from fastapi import APIRouter, HTTPException, Query
from database import db
from models import Book
from bson import ObjectId
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

# ✅ Pydantic Model for Paginated Response
class PaginatedBooksResponse(BaseModel):
    total_books: int
    total_pages: int
    current_page: int
    books: List[Book]

# ✅ Get Books with Pagination, Search & Filter
@router.get("/books", response_model=PaginatedBooksResponse)
async def get_books(
    title: Optional[str] = Query(None, description="Search by book title", example="Harry Potter"),
    author: Optional[str] = Query(None, description="Search by author", example="J.K. Rowling"),
    published_year: Optional[int] = Query(None, description="Filter by published year", example=2000),
    page: int = Query(1, ge=1, description="Page number (starts from 1)", example=1),
    limit: int = Query(10, ge=1, le=50, description="Books per page (max 50)", example=5)
):
    books_collection = db["books"]
    query = {}

    # 🔍 Apply Search & Filters
    if title:
        query["title"] = {"$regex": title, "$options": "i"}  # Case-insensitive
    if author:
        query["author"] = {"$regex": author, "$options": "i"}
    if published_year:
        query["published_year"] = published_year

    # 📌 Pagination
    skip_count = (page - 1) * limit  
    books = await books_collection.find(query).skip(skip_count).limit(limit).to_list(limit)

    # 📊 Total Count
    total_books = await books_collection.count_documents(query)
    total_pages = (total_books // limit) + (1 if total_books % limit > 0 else 0)

    return {
        "total_books": total_books,
        "total_pages": total_pages,
        "current_page": page,
        "books": books
    }

# ✅ Add a New Book
@router.post("/books")
async def create_book(book: Book):
    books_collection = db["books"]
    result = await books_collection.insert_one(book.dict())
    return {"message": "Book added successfully", "id": str(result.inserted_id)}

# ✅ Define a Model for Partial Updates
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None

# ✅ PATCH (Partial Update)
@router.patch("/books/{book_id}")
async def patch_book(book_id: str, book: BookUpdate):
    books_collection = db["books"]

    try:
        obj_id = ObjectId(book_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid book ID format")

    updated_data = {k: v for k, v in book.dict().items() if v is not None}

    if not updated_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    result = await books_collection.update_one({"_id": obj_id}, {"$set": updated_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book updated successfully"}

# ✅ DELETE (Remove a Book)
@router.delete("/books/{book_id}")
async def delete_book(book_id: str):
    books_collection = db["books"]

    # 🔍 Validate the ObjectId format
    try:
        obj_id = ObjectId(book_id)
    except Exception as e:
        print(f"❌ Invalid ObjectId: {book_id} | Error: {e}")  # Log the error
        raise HTTPException(status_code=400, detail="Invalid book ID format (must be a 24-character hex string)")

    # 🔍 Check if the book exists before deleting
    existing_book = await books_collection.find_one({"_id": obj_id})
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    # ❌ Try deleting the book
    result = await books_collection.delete_one({"_id": obj_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=500, detail="Failed to delete book (unknown error)")

    return {"message": "Book deleted successfully", "deleted_id": book_id}