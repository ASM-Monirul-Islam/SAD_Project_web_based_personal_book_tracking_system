from django.urls import path
from .import views
urlpatterns = [
	path('home/', views.home, name='home'),
	# path('book_list/<slug:slug>', views.book_list, name='book_list'),

]
