from django.shortcuts import render,redirect,get_object_or_404
from .models import offerings
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import offerings



# Create your views here.

def course(request,slug):
    course = get_object_or_404(offerings, slug=slug)
    return render(request,'courses/course.html',{'course':course})