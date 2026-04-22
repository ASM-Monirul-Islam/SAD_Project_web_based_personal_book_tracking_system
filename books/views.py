from django.shortcuts import render, get_object_or_404
from books.models import Book


# Create your views here.
def view_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
		'book':book
	}
    return render(request, 'books/view_book.html', context)
