from books import *

def update_id(Books: list, book: Book) -> Book:
    '''
    Retorna o livro criado com o "id" correto
    '''
    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book

    # if len(Books) > 0:
    #     book.id = Books[-1].id + 1
    # else:
    #     book.id = 1
    # return book

def get_book_id(id: int, Books: list):
    for book in Books:
        if book.id == id:
            return book
        
def book_to_update(book_request: Book, Books: list):
    for i in range(len(Books)):
        if Books[i].id == book_request.id:
            Books[i] = book_request

def book_to_delete(id: int, Books: list):
    for i in range(len(Books)):
        if Books[i - 1].id == id:
            Books.pop(i)
            break