from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Profile



def login_page(request):
	if request.method=='POST':

		username = request.POST.get('email')
		password = request.POST.get('password')

		user_obj = User.objects.filter(username=username)

		if not user_obj.exists():
			messages.warning(request, 'Account Not Found')
			return HttpResponseRedirect(request.path_info)
		
		elif not user_obj[0].profile.is_email_verified:
			messages.warning(request, 'Your Account is not verified, Verification link sent to your email')
			return HttpResponseRedirect(request.path_info)
		
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			if user.is_superuser:
				return redirect('/admin/')	
			return redirect('home')
		else:
			messages.warning(request, 'Your password is not Correct')
			return HttpResponseRedirect(request.path_info)

	return render(request, 'accounts/login.html', {})

def register_page(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		pass1 = request.POST.get('pass1')
		pass2 = request.POST.get('pass2')

		if pass1 != pass2:
			messages.warning(request, 'Passwords do not match')
			return HttpResponseRedirect(request.path_info)

		if len(pass1)<8:
			messages.warning(request, "Password length can't be less than 8 digits")
			return  HttpResponseRedirect(request.path_info)

		if not validate_email(email):
			messages.warning(request, "Enter a valid email address")
			return HttpResponseRedirect(request.path_info)
		
		if User.objects.filter(username=email).exists():
			messages.warning(request, 'This Email is already in use')
			return HttpResponseRedirect(request.path_info)
		
		user = User.objects.create_user(
			username=email,
			email=email,
			password=pass1
		)

		user.save()

		messages.success(request, 'A verification mail has been sent to your Email')
		return redirect('login')

	return render(request, 'accounts/register.html', {})

@require_POST
def logout_user(request):
	logout(request)
	return redirect('login')

def activate_account(request, email_token):
	try:
		user = Profile.objects.get(email_token = email_token)
		user.is_email_verified=True
		user.save()
		messages.success(request, 'You can now login')
		return redirect('login')
	except Exception as e:
		print(e)
  
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
		'profile':profile
	}
    return render(request, 'accounts/profile.html', context)

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method=='POST':
        user=request.user
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.phone = request.POST.get('phone')
        profile.bio = request.POST.get('bio')
        profile.interests = request.POST.get('interests')
        profile.fav_quotes = request.POST.get('fav_quotes')
        
        if request.FILES.get('image'):
            profile.image=request.FILES['image']
        
        
        profile.save()
        return redirect('profile')
    context = {
		'profile':profile
	}
    return render(request, 'accounts/edit_profile.html', context)
