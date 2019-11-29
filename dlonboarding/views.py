from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])

                return render(request, 'dlonboarding/signup.html', {'error': 'Username already exist'})


            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'dlonboarding/signup.html', {'error': 'Password should match'})
    else:
        return render(request, 'dlonboarding/signup.html')


def userhome(request):
    return render(request,'dlonboarding/home.html')

def newblog(request):
    return render(request,'dlonboarding/newblog.html')