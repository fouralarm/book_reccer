import requests
import os
from dotenv import load_dotenv

load_dotenv()
books_api_key = os.getenv("BOOKS_API_KEY")


def get_book_metadata(api_key, query):
    """
    Fetch metadata for a book using the Google Books API.

    :param api_key: Your Google Books API key.
    :param query: The search query (e.g., book title, author, ISBN).
    :return: Metadata about the book.
    """
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,  # Search query
        "key": api_key  # API key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            return data["items"]
        else:
            return "No books found for the given query."
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
if __name__ == "__main__":
    API_KEY = books_api_key
    bookname = "The Da Vinci Code dan brown"

    books = get_book_metadata(API_KEY, bookname)
    if isinstance(books, list):
        for book in books:
            print(book.keys())
            print(book['volumeInfo'].keys())
            print(f"Title: {book['volumeInfo'].get('title', 'N/A')}")
            print(f"Authors: {book['volumeInfo'].get('authors', 'N/A')}")
            #print(f"Publisher: {book['volumeInfo'].get('publisher', 'N/A')}")
            print(f"Published Date: {book['volumeInfo'].get('publishedDate', 'N/A')}")
            print(f"Description: {book['volumeInfo'].get('description', 'N/A')}")
            print(f"Page Count: {book['volumeInfo'].get('pageCount', 'N/A')}")
            print(f"Categories: {book['volumeInfo'].get('categories', 'N/A')}")
            print(f"Language: {book['volumeInfo'].get('language', 'N/A')}")
            print("-" * 40)
    else:
        print(books)