from django.shortcuts import render,redirect,get_object_or_404
from .models import offerings
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template.defaultfilters import slugify
from .models import offerings
# Create your views here.



