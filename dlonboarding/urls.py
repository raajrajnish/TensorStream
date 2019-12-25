from django.urls import path
from  . import views


urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('userhome',views.userhome,name='userhome'),

]
