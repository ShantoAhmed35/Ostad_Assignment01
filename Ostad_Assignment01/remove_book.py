from book_data import load_books, save_books

def remove_book():
    """Remove a book by ISBN."""
    books = load_books()
    
    isbn = input("Enter the ISBN of the book to remove: ")
    
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return
    
    print("Error: Book not found.")