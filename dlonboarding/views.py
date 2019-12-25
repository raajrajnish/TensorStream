from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from dlblog.models import Blog


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def signup(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'dlonboarding/signup.html', {'error': 'Opps..username is not unique!'})

            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],
                                                email=request.POST['email'])
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
        else:
            return render(request, 'dlonboarding/signup.html', {'error': 'Password should match'})
    else:
        return render(request, 'dlonboarding/signup.html')


@login_required
def userhome(request):
    userblog = Blog.objects.filter(author=request.user)
    return render(request, 'dlonboarding/userhome.html',{'currentuserblogs':userblog})


def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        # if user is present
        if user is not None:
            # do the login
            auth.login(request,user)
            # if user is present and enters valid credentials
            userblog = Blog.objects.filter(author=request.user)
            return render(request,'dlonboarding/userhome.html',{'user':user,'currentuserblogs':userblog})
        else:
            return render(request,'dlonboarding/signin.html',{'error':"Please enter valid Credentials!"})
    else:
        return render(request, 'dlonboarding/signin.html',{'error':"Please enter valid Credentials!"})
