from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,UseCase
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone
from django.template.defaultfilters import slugify
from .forms import addMainContent


# Create your views here.

def home(request):
    return render(request,'dlblog/home.html',{'blog':Blog.objects.all()[0:3],'usecase':UseCase.objects.all()[0:3]})

def blogs(request):
    return render(request,'dlblog/blogs.html',{'blog':Blog.objects.all()})


def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])


        # if user is present
        if user is not None:
            # do the login
            auth.login(request,user)
            # if user is present and enters valid credentials
            return render(request,'dlonboarding/home.html',{'user':user})
        else:
            return render(request,'dlblog/home.html',{'error':"Please enter valid Credentials!"})
    else:
        return render(request, 'dlblog/home.html',{'error':"Please enter valid Credentials!"})

@login_required
def newblog(request):
    return render(request,'dlblog/newblog.html')

'''


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
            blog.slug = slugify(request.POST['title'])
            # Fields 5 Blog Author.
            blog.author = request.user
            # Fields 6 Blog Content
            blog.content = request.POST['content']
            blog.save()
            return redirect('/dlblog/' + blog.slug)

        else:
            return render(request, 'dlblog/newblog.html', {'error': 'Please enter all details'})
    else:
        return render(request, 'dlblog/newblog.html')


'''

@login_required
def create(request):
    if request.method == "POST":
        form = addMainContent(request.POST,request.FILES)
        print("Form is : ",form)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author =  request.user
            instance.slug = slugify(request.POST['title'])
            instance.save()
            return redirect('home')
    else:
        form = addMainContent()

    return render(request, 'dlblog/newblog.html',{'form':form})





def blog_home(request,slug):
    print("blog_home ----")
    blog = get_object_or_404(Blog, slug=slug)
    return render(request,'dlblog/blog_home.html',{'blog': blog})


