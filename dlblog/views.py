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
    only_pub_blog = Blog.objects.filter(status=1)
    ony_pub_ucase = UseCase.objects.all()[0:6]
    return render(request,'dlblog/home.html',{'blog':only_pub_blog[0:6],'usecase':ony_pub_ucase})

def blogs(request):
    only_pub_blog = Blog.objects.filter(status=1)
    return render(request,'dlblog/blogs.html',{'blog':only_pub_blog})


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
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author =  request.user
            instance.slug = slugify(request.POST['title'])
            instance.save()
            return redirect('home')
    else:
        form = addMainContent()
    return render(request, 'dlblog/newblog.html',{'form':form})


@login_required
def edit_blog(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == "POST":
        form = addMainContent(request.POST or None,instance=blog)
        try:
            if form.is_valid():
                form.content.save()
                print('executed save')
                return redirect('home')
        except Exception as e:
            print("Error :", e)
    else:
        form = addMainContent(instance=blog)
        slug = blog.slug

    return render(request, 'dlblog/editblog.html', {'form': form,'slug':slug})


def blog_home(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request,'dlblog/blog_home.html',{'blog': blog})

