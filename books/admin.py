from django.contrib import admin
from .models import Book, Genre
# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
