from django.urls import path,include
from  . import views


urlpatterns = [
    path('create',views.create,name='create'),
    path('login',views.login,name='login'),
    path('<slug:slug>/',views.blog_home,name='blog_home'),
    path('blogs',views.blogs,name='blogs'),
    path('newblog',views.newblog,name='newblog'),
]
