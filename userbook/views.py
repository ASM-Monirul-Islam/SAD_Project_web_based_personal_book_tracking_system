from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from userbook.models import UserBook
from books.models import Book
from accounts.models import Profile
from django.views.decorators.http import require_POST


# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from books.models import Book
from .models import UserBook


@login_required
def add_to_wishlist(request, slug):
    if request.method == "POST":
        book = get_object_or_404(Book, slug=slug)

        userbook, created = UserBook.objects.get_or_create(
            user=request.user,
            book=book,
            defaults={'status': 'Wishlist'}
        )

        if not created:
            # already exists → just update status
            userbook.status = 'Wishlist'
            userbook.save()
            messages.warning(request, "Already in your list. Status updated to Wishlist.")
        else:
            messages.success(request, "Added to Wishlist.")

    return redirect(request.META.get('HTTP_REFERER')) 


def mybook(request):
    books = Book.objects.all()
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'userbook/mybook.html', {'books':books, 'profile':profile})


@require_POST
def change_status(request, slug):
    book = get_object_or_404(Book, slug=slug)
    user_book = get_object_or_404(UserBook, book=book)
    if request.method=='POST':
        status = request.POST.get('status')
    valid_status = [choice[0] for choice in UserBook.STATUS_CHOICES]
    if status in valid_status:
        user_book.status=status
        if status=='Wishlist':
            user_book.wishlist=True
            user_book.reading=False
            user_book.completed=False
        elif status=='Reading':
            user_book.wishlist=False
            user_book.reading=True
            user_book.completed=False
        else:
            user_book.wishlist=False
            user_book.reading=False
            user_book.completed=True
        user_book.save()
        messages.success(request, f'Book Status Updated to {status}')
    return redirect(request.META.get('HTTP_REFERER'))


def delete_userbook(request, slug):
    book = get_object_or_404(Book, slug=slug)
    user_book = get_object_or_404(UserBook, book=book)
    user_book.delete()
    messages.success(request, f'Removed {book.title} Successfully')
    return redirect(request.META.get('HTTP_REFERER'))

def rate_book(request, slug):
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        book = get_object_or_404(Book, slug=slug)
        user_book = get_object_or_404(UserBook, book=book)
        user_book.rating = rating
        user_book.save()
        messages.success(request, f'Rating Updated to {rating} Star')
    return redirect(request.META.get('HTTP_REFERER'))