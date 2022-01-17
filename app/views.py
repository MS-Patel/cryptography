from django.http.response import HttpResponse
from django.shortcuts import  redirect, render

from account.models import Account
from .models import Coin, UserPortfolio

def home(request):
    return render(request,'index.html')

def userprofile(request):
    if request.method == 'POST':
        obj=Account.objects.get(id=request.user.id)
        obj.username=request.POST['fname']
        obj.lname=request.POST['lname']
        obj.phone=request.POST['pnum']
        obj.address=request.POST['address']
        obj.save()
    list=Account.objects.all()
    return render(request,'user/userprofile.html',{'list':list})

def userdashboard(request):
    list=UserPortfolio.objects.filter(user=request.user)
    alist=Coin.objects.last()
    return render(request,'user/userdashboard.html',{'list':list,'alist': alist})

def adminbase(request):
    return render(request,'admin/admin.html')    

def admindashboard(request):
    
    return render(request,'admin/admindashboard.html')

def adminprofile(request):
    if request.method == 'POST':
        obj= Account.objects.get(id=request.user.id)
        obj.username=request.POST['fname']
        obj.email=request.POST['email']
        obj.date_joined=request.POST['date_joined']
        obj.last_login=request.POST['last_login']
        obj.lname=request.POST['lname']
        obj.phone=request.POST['pnum']
        obj.address=request.POST['address']
        obj.save()
    list=Account.objects.all()
    port=UserPortfolio.objects.all()
    return render(request,'admin/adminprofile.html',{'list':list,"port":port})        

def adminctsdetails(request):

    data = Account.objects.all() 

    return render(request,'admin/adminctsdetails.html',{"users":data})        

def adminNAV(request):
    list=Coin.objects.last()
    return render(request,'admin/adminNAV.html',{'list':list})             

def coin(request):
    if request.method=='POST':
        obj = Coin()
        obj.nav = request.POST['nav']
        obj.save()
        return redirect('app:adminNAV')
    return HttpResponse('/')
    