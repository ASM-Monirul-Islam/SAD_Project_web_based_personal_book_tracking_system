import requests
from books.models import Book, Genre
from django.utils.text import slugify


GOOGLE_BOOKS_API = "https://www.googleapis.com/books/v1/volumes?q="


def fetch_books_from_google(query):
    url = GOOGLE_BOOKS_API + query
    response = requests.get(url)
    data = response.json()

    books = []

    for item in data.get("items", []):
        info = item.get("volumeInfo", {})

        title = info.get("title")
        authors = info.get("authors", ["Unknown"])
        published_date = info.get("publishedDate", "Unknown")
        language = info.get("language", "en")
        description = info.get("description", "")
        
        # Image handling
        image_links = info.get("imageLinks", {})
        image = image_links.get("thumbnail", None)

        book_data = {
            "title": title,
            "slug": slugify(title),
            "author": ", ".join(authors),
            "publication_year": published_date[:4] if published_date else "Unknown",
            "language": language,
            "description": description,
            "image": image,
        }

        books.append(book_data)

    return books

def save_books_to_db(books, genre_id):
    genre = Genre.objects.get(id=genre_id)

    for b in books:
        if not Book.objects.filter(slug=b["slug"]).exists():
            Book.objects.create(
                title=b["title"],
                slug=b["slug"],
                author=b["author"],
                publication_year=b["publication_year"],
                language=b["language"],
                description=b["description"],
                genre=genre,
                book_image=b["image"]
            )