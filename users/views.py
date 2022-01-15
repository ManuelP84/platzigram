"""User views."""

#Django
from pdb import set_trace
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Models
from django.contrib.auth.models import User
from users.models import Profile

#Exceptions
from django.db import IntegrityError

#Forms
from users.forms import ProfileForm

@login_required
def update_profile(request):
    """Update a user's profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()
    
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form
        }
    )


def login_view(request):
    """Login an user"""
    
    if request.method == 'POST':        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        print(user)
               
        if user:
            
            login(request, user)
            return redirect('feed') # 'feed' is the name of the path. In case the URL change in the future
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and/or password'})


    return render(request, 'users/login.html')


def signup(request):
    """Sign up view"""
    #import pdb; set_trace()
    #Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password == passwd_confirmation:
            try:
                user = User.objects.create_user(
                    username=username, 
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'Username already exists'})
            profile = Profile(user=user)
            profile.save()

            return redirect('login')
        else:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Logout an user"""
    logout(request)
    return redirect('login')


