from django.shortcuts import render,redirect
from .models import Blog,UseCase
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def home(request):
    return render(request,'dlblog/home.html',{'blog':Blog.objects.all()[0:3],'usecase':UseCase.objects.all()[0:3]})

def blogs(request):
    return render(request,'dlblog/blogs.html',{'blog':Blog.objects.all()})

def blog_home(request):
    return render(request,'dlblog/blog_home.html')


def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])

        if user is not None:
            auth.login(request,user)
            return render(request,'dlonboarding/home.html',{'error':'Username or Password is Incorrect!'})
        else:
            return render(request,'dlblog/home.html',{'user':user})
    else:
        return render(request, 'dlblog/home.html')

