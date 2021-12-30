from . import views
from django.urls import path

app_name = "app"

urlpatterns = [
    path('', views.home),
    path('login', views.login,name='login'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('userdashboard',views.userdashboard,name='userdashboard'),
    path('adminbase',views.adminbase,name='adminbase'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('adminprofile',views.adminprofile,name='adminprofile'),
    
]
 