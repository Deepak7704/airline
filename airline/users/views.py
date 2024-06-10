from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/index.html")

def login_view(request):
    if request.method=="POST":
        username=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        return render(request,"users/login.html",{
            "message":"Invalid Credentials"
        })
    return render(request,"users/login.html") 


def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message":"user have logged out"
    })