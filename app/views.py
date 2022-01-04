from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Coin

def home(request):
    return render(request,'index.html')

def login(request):
    # authenticare user credensials:

    # after login redirect to userdashboard
    return redirect('app:userdashboard')   

def userprofile(request):
    return render(request,'user/userprofile.html')

def userdashboard(request):
    return render(request,'user/userdashboard.html')

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
    