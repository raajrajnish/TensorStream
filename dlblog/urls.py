from django.urls import path,include
from  . import views


urlpatterns = [
    path('login',views.login,name='login'),
    path('blog_home',views.blog_home,name='blog_home'),
    path('blogs',views.blogs,name='blogs'),
]
