from django.shortcuts import render, get_object_or_404
from accounts.models import Profile
from userbook.models import UserBook
from books.models import Book, Genre
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.
# def home(request):
#     profile = get_object_or_404(Profile, user=request.user)
#     genres = Genre.objects.all()

#     status = request.GET.get('status', 'All')
    
#     if status == 'All':
#         user_books = Book.objects.all()
#     if status != 'All':
#         user_books = UserBook.objects.filter(user=request.user, status=status)

#     context = {
#         'profile': profile,
#         'user_books': user_books,
#         'genres': genres,
#         'active_status': status,
#     }

#     return render(request, 'homepage/home.html', context)



def home(request):
    profile = get_object_or_404(Profile, user=request.user)
    genres = Genre.objects.all()

    status = request.GET.get('status', 'All')
    query = request.GET.get('q', '')

    if status == 'All':
        user_books = Book.objects.all()

        # 🔍 SEARCH FILTER (IMPORTANT PART)
        if query:
            user_books = user_books.filter(
                title__icontains=query
            ) | user_books.filter(
                author__icontains=query
            )

    else:
        user_books = UserBook.objects.filter(
            user=request.user,
            status=status
        )

        # optional search inside user books too
        if query:
            user_books = user_books.filter(
                book__title__icontains=query
            ) | user_books.filter(
                book__author__icontains=query
            )

    context = {
        'profile': profile,
        'user_books': user_books,
        'genres': genres,
        'active_status': status,
        'search_query': query   # 🔥 send to template
    }

    return render(request, 'homepage/home.html', context)