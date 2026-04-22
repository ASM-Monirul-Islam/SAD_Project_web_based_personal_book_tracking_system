from django.urls import path
from .import views

urlpatterns = [
	path('', views.login_page, name='login'),
	path('register/', views.register_page, name='register'),
	path('logout/', views.logout_user, name='logout'),
	path('activate/<email_token>', views.activate_account, name='activate_account'),
	path('profile/', views.profile, name='profile'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
]
