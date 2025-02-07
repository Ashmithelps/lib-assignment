import React, { useEffect, useState } from "react";
import AddBook from "../components/AddBook";

const Books = () => {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [editingBook, setEditingBook] = useState(null);

  // Fetch books from backend
  const fetchBooks = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/books");
      if (!response.ok) {
        throw new Error("Failed to fetch books");
      }
      const data = await response.json();
      setBooks(data.books);
    } catch (error) {
      setError(error.message);
    }

    setLoading(false);
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  // ✅ Handle Delete Book (100% Working)
  const handleDelete = async (id, e) => {
    if (e) e.preventDefault(); // Prevent form submission
    
    console.log("🟡 Delete button clicked for ID:", id); // Debugging log

    if (!id) {
        console.error("❌ Error: Book ID is undefined!");
        return;
    }

    try {
        console.log("🟡 Sending DELETE request..."); // Debugging log
        const response = await fetch(`http://localhost:8000/books/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        });

        console.log("🟡 DELETE request sent:", response); // Debugging log

        if (!response.ok) {
            const errorData = await response.json();
            console.error("❌ Delete failed:", errorData);
        } else {
            console.log("✅ Book deleted successfully");

            // Remove book from UI
            setBooks((prevBooks) => prevBooks.filter((book) => book.id !== id));
        }
    } catch (error) {
        console.error("❌ Network error:", error);
    }
};



  // Handle Edit Book
  const handleEdit = (book) => {
    setEditingBook(book);
  };

  return (
    <div>
      <h1>Books Collection</h1>
      <AddBook onBookAdded={fetchBooks} />

      <h2>Available Books</h2>
      {loading && <p>Loading books...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul>
  {books.map((book, index) => {
    console.log(`📘 Book ${index}:`, book); // Debugging log
    return (
      <li key={book.id || book._id || index}>
        {book.title} by {book.author} ({book.published_year}){" "}
        <button type="button" onClick={() => handleDelete(book.id)}>Delete</button>
      </li>
    );
  })}
</ul>



    </div>
  );
};

export default Books;
