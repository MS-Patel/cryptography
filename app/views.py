from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'user/users.html')   

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