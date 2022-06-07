from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       min_length=1,
                                       max_length=100)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "d1661184-d342-479c-a70c-de0976cb20e2",
                "title": "Computer Science",
                "author": "Miguel",
                "description": "Coding beautifully",
                "rating": 75
            }
        }


BOOKS = []


# It returns either all the books or at least the maximum quantity of books passed via parameter
@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i += 1
        return new_books
    return BOOKS


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    book_1 = Book(id="d1661184-d342-479c-a70c-de0976cb20e7",
                  title="Title 1",
                  author="Author 1",
                  description = "Description 1",
                  rating=50)
    book_2 = Book(id="d1661184-d342-479c-a70c-de0976cb20e7",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=80)
    book_3 = Book(id="d1661184-d342-479c-a70c-de0976cb20e7",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=90)
    book_4 = Book(id="d1661184-d342-479c-a70c-de0976cb20e7",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=70)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)

