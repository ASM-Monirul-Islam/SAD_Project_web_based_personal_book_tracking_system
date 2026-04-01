from django.urls import path
from .import views

urlpatterns = [
	path('view_books/', views.home, name='view_books'),
]
