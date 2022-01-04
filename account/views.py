from django.http.response import HttpResponse
from django.shortcuts import redirect

from .models import Account
# Create your views here.

from django.contrib.auth import authenticate, logout as lgout, login as lg

def login(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        pwd = request.POST['password']
        user = authenticate(request,username=email,password=pwd)
        if user is not None:
            lg(request, user)
            if user.is_verified:
                return redirect('app:userdashboard')
            return HttpResponse("please wait 24hours untill your account is verified")   
    return redirect('app:home')

def logout(request):
    lgout(request)

    return redirect("app:home")

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email_id']
        pwd = request.POST['password']
        new_user = Account.objects.create_user(email,username, pwd)
        new_user.save()
    return redirect('account:login') 