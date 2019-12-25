from django.urls import path,include
from  . import views


urlpatterns = [
    path('create',views.create,name='create'),
    path('<slug:slug>/',views.blog_home,name='blog_home'),
    path('blogs',views.blogs,name='blogs'),
    path('newblog',views.newblog,name='newblog'),
    path('edit_blog/<slug:slug>/',views.edit_blog,name='edit_blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
