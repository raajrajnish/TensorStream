from django.urls import path
from  . import views


urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('userhome',views.userhome,name='userhome'),
    path('newblog',views.newblog,name='newblog'),
]
