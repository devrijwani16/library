from fastapi import APIRouter, Response
from models.bookModel import book
from controllers.bookController import create_book_controller, get_book_controller, update_book_controller, delete_book_controller, get_books_id_controller

bookRouter = APIRouter(
    # means every route inside this router automatically starts with /books.
    prefix= '/books',
    tags= ['books']
    # This grps all api under group named books : Organized
)
# books = []
# id = 0

# Create book
@bookRouter.post('/postbooks')
def create_book(book: book, response: Response):
    return create_book_controller(book, response)

# Get books
@bookRouter.get('/getbooks')
def get_books(response: Response):
    return get_book_controller(response)

# Get book by ID
@bookRouter.get('/getbook/{bookid}')
def get_books_id(bookid: int, response: Response):
    return get_books_id_controller(bookid, response)

# Delete book
@bookRouter.delete('/deletebook/{bookid}')
def delete_book(bookid: int, response: Response):
    return delete_book_controller(bookid, response)

# Update book
@bookRouter.put('/updatebook/{bookid}')
def update_book(bookid: int,updated_book: book, response: Response):
    return update_book_controller(bookid, updated_book, response)
#### All str for mongoDb id:int to id:str