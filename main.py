from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session
import models
from database import engine, Base, SessionLocal


app = FastAPI()

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class BookCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str =Field(min_length=1)
    author: str =Field(min_length=1)
    published_year: int =Field(gt=0, le=2026)
    genre: str =Field(min_length=1)

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    published_year: int
    genre: str

    model_config = ConfigDict(from_attributes=True)

class DeleteResponse(BaseModel):
    message: str

class UpdateResponse(BaseModel):
    message: str
    book: BookResponse


@app.get("/")
def home():
    return {"message": "Welcome to the Book Management API"}


@app.post("/books", response_model=BookResponse, status_code=201)
def add_book(book:BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(
        title=book.title,
        author=book.author,
        published_year=book.published_year,
        genre=book.genre
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book
        
@app.get("/books", response_model=list[BookResponse])
def get_books(db:Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db:Session = Depends(get_db)):
    book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return book
   
@app.put("/books/{book_id}", response_model=UpdateResponse)
def update_book(
    book_id: int, 
    updated_book: BookCreate,
    db:Session = Depends(get_db)
    ):

    book = db.query(models.Book).filter(
        models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    
    book.title = updated_book.title
    book.author = updated_book.author
    book.published_year = updated_book.published_year
    book.genre = updated_book.genre

    db.commit()
    db.refresh(book)
            
    return{
        "message": "Book updated successfully",
        "book":book
    }

@app.delete("/books/{book_id}", response_model=DeleteResponse)
def delete_book(book_id:int, db:Session = Depends(get_db)):
    book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    db.delete(book)
    db.commit()

    return{
        "message": "Book deleted successfully"
    }