from django.http.response import HttpResponse
from django.shortcuts import  redirect, render

from account.models import Account
from .models import Coin, Feedback, UserPortfolio

from django.contrib import messages
from .forms import FeedbackForm

def home(request):
    return render(request,'index.html')

def userprofile(request):
    if request.method == 'POST':
        obj=Account.objects.get(id=request.user.id)
        obj.username=request.POST['fname']
        obj.lname=request.POST['lname']
        obj.phone=request.POST['pnum']
        obj.address=request.POST['address']
        obj.tgid=request.POST['tgid']
        obj.save()
    list=Account.objects.get(id=request.user.id)
    return render(request,'user/userprofile.html',{'list':list})

def userdashboard(request):
    list=UserPortfolio.objects.filter(user=request.user)
    alist=Coin.objects.last()
    return render(request,'user/userdashboard.html',{'list':list,'alist': alist})

def faq(request):

    return render (request,'user/faq.html')    

def adminbase(request):
    return render(request,'admin/admin.html')    

def admindashboard(request):
    
    return render(request,'admin/admindashboard.html')

def adminctsdetails(request):

    data = Account.objects.all() 

    return render(request,'admin/adminctsdetails.html',{"users":data})   

def adminprofile(request,id):
    if request.method == 'POST':
        obj= Account.objects.get(id=id)
        if 'is_verified' in request.POST:
           obj.is_verified = True
        else:
           obj.is_verified = False
        obj.username=request.POST['username']
        obj.phone=request.POST['pnum']
        obj.save()
        return redirect("app:adminctsdetails")
    list=Account.objects.get(id=id)
    port=UserPortfolio.objects.filter(user=list)
    return render(request,'admin/adminprofile.html',{'list':list,"port":port})        

     

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
    



def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('app:feedback')
    else:
        f = FeedbackForm()
    return render(request, 'user/c&s.html', {'form': f})

def adminsupport(request):

        data = Feedback.objects.all()

        return render(request,'admin/adminsupport.html',{'f':data})