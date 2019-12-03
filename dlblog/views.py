from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,UseCase
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone


# Create your views here.

def home(request):
    return render(request,'dlblog/home.html',{'blog':Blog.objects.all()[0:3],'usecase':UseCase.objects.all()[0:3]})

def blogs(request):
    return render(request,'dlblog/blogs.html',{'blog':Blog.objects.all()})


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

@login_required
def newblog(request):
    return render(request,'dlblog/newblog.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.FILES['blog_main_image'] and request.POST['title'] and request.POST['summary'] and request.POST['content']:
            blog = Blog()
            # Fields 1 Blog Image.
            blog.blog_main_image = request.FILES['blog_main_image']
            # Fields 2 Blog Title.
            blog.title = request.POST['title']
            # Fields 3 Blog Summary.
            blog.summary = request.POST['summary']
            # Fields 4 Blog Slug.
            blog.slug = request.POST['title']
            # Fields 5 Blog Author.
            blog.author = request.user
            # Fields 6 Blog Content
            blog.content = request.POST['content']

            blog.save()
            return redirect('/dlblog/' + str(blog.id))

        else:
            return render(request, 'dlblog/newblog.html', {'error': 'Please enter all details'})
    else:
        return render(request, 'dlblog/newblog.html')

def blog_home(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'dlblog/blog_home.html',{'blog': blog})