from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    _id: Optional[str]  
    title: str
    author: str
    published_year: int
    isbn: Optional[str] = None
