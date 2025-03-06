from book_data import load_books, save_books

def add_book():
    """Add a new book to the store."""
    books = load_books()
    
    print("\nAdd a New Book")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")
    genre = input("Enter the genre: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity in stock: "))

    # Check for duplicate ISBN
    for book in books:
        if book["isbn"] == isbn:
            print("Error: A book with this ISBN already exists.")
            return

    # Add the new book
    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "genre": genre,
        "price": price,
        "quantity": quantity
    }
    books.append(new_book)
    save_books(books)
    print("Book added successfully!")