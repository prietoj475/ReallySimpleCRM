from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'auth/register.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(first_name=request.POST['firstname'], last_name=request.POST['lastname'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('contacts:listcontacts')

            except IntegrityError:
                return render(request, 'auth/register.html', {'form':UserCreationForm(), 'error': 'That username ahas already been taken. Please choose a new username'})
        else:
            return render(request, 'auth/register.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'auth/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('contacts:listcontacts')
        
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:loginuser')
