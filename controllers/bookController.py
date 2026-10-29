from fastapi import APIRouter, Response
from models.bookModel import book
# from dbConnect import bookCollection
# from bson import ObjectId

books = []
id = 0

def create_book_controller(book: book, response: Response):
    global id
    try:
        id += 1
        book.id = id
        books.append(book)
        response.status_code = 201
        return {'isSuccess':True, 'message' : 'book Created Successfully', 'book': book}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}

def get_books_id_controller(bookid: int, response: Response):
    try:
        response.status_code = 200
        for book in books:
            if book.id == bookid:
                return {'isSuccess': True, 'book': book}

        response.status_code = 404
        return {'isSuccess':False, 'message' : 'book not found'}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}

def get_book_controller(response: Response):
    try:
        response.status_code = 200
        return {'isSuccess':True, 'message' : 'book Display Successfully', 'books': books}
    except Exception as e:
        response.status_code = 500
        return{'isSuccess' : False, 'message' : str(e)}

def delete_book_controller(bookid:int, response:Response):
    try:
        response.status_code = 200
        for book in books:
            if book.id == bookid:
                books.remove(book)
                return {'isSuccess' : True, 'messege' : 'book deleted successfully'}
        response.status_code = 404
        return {'message' : 'book not found', 'isSuccess' : False}
    except Exception as e:
        print(e)
        response.status_code = 500
        return{'isSuccess' : False, 'message' : 'Error Creating book'}

def update_book_controller(bookid: int,updated_book: book, response: Response):
    try:
        response.status_code = 200
        for book in books:
            if book.id == bookid:
                book.book_name = updated_book.book_name
                book.author = updated_book.author
                book.publication = updated_book.publication
                book.year = updated_book.year

                return {'isSuccess': True, 'message': 'book Updated Successfully', 'book': book}

        response.status_code = 404
        return {'isSuccess': False, 'message': 'book not found'}

    except Exception as e:
        response.status_code = 500
        return {'isSuccess': False, 'message': str(e)}

