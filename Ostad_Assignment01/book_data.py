import json
import os

# File path for storing book data
BOOKS_FILE = "books.json"

def load_books():
    """Load books from the JSON file."""
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    """Save books to the JSON file."""
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)