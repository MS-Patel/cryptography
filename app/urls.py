from . import views
from django.urls import path

app_name = "app"

urlpatterns = [
    path('', views.home, name="home"),
    path('coin', views.coin, name="coin"),
    path('userprofile',views.userprofile,name='userprofile'),
    path('userdashboard',views.userdashboard,name='userdashboard'),
    path('adminbase',views.adminbase,name='adminbase'),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('adminctsdetails',views.adminctsdetails,name='adminctsdetails'),
    path('adminNAV',views.adminNAV,name='adminNAV'),
    path('faq',views.faq,name='faq'),
    path('2FA',views.TFA,name='2FA' ),
    path('feedback', views.feedback, name='feedback'),
    path('adminsupport', views.adminsupport, name='adminsupport'),
    path('user/<int:id>/',views.adminprofile,name='adminprofile'),
    
]
 