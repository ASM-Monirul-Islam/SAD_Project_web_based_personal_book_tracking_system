from django.urls import path
from .import views

urlpatterns = [
    path('add_to_wishlist/<slug:slug>', views.add_to_wishlist, name='add_to_wishlist'),
	path('mybook/', views.mybook, name='mybook'),
	path('change_status/<slug:slug>', views.change_status, name='change_status'),
	path('delete_userbook/<slug:slug>', views.delete_userbook, name='delete_userbook'),
	path('rate_book/<slug:slug>', views.rate_book, name='rate_book'),
]
