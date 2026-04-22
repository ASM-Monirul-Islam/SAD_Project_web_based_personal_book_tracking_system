from django.urls import path
from .import views

urlpatterns = [
	path('view_book/<slug:slug>', views.view_book, name='view_book'),
]
