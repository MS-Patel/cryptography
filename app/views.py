from django.http.response import HttpResponse
from django.shortcuts import  render
from .models import Coin, UserPortfolio

def home(request):
    return render(request,'index.html')

def userprofile(request):
    return render(request,'user/userprofile.html')

def userdashboard(request):
    list=UserPortfolio.objects.get(user=request.user)
    return render(request,'user/userdashboard.html',{'list':list})

def adminbase(request):
    return render(request,'admin/admin.html')    

def admindashboard(request):
    return render(request,'admin/admindashboard.html')     

def adminprofile(request):
    return render(request,'admin/adminprofile.html')        

def adminctsdetails(request):
    return render(request,'admin/adminctsdetails.html')        

def adminNAV(request):
    return render(request,'admin/adminNAV.html')        

def coin(request):
    if request.method=='POST':
        obj = Coin()
        obj.nav = request.POST['nav']
        obj.save()
        return HttpResponse('Successful')
    return HttpResponse('/')
    