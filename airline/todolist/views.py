from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User,Goals,Tasks
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,"todolist/index.html")

def register(request):
    if request.method=="POST":
        nameinput=request.POST['username']
        emailinput=request.POST['email']
        passwordinput=request.POST['password']
        confirmationinput=request.POST['confirmation']

        #Ensuring to match password and confirm password
        if(passwordinput != confirmationinput):
            return render(request,"todolist/register.html",{
                "message":"password doesn't match with confirm password"
            })
        #Attempting to create a new user
        try:
            user=User.objects.create_user(nameinput,emailinput,passwordinput)
            user.save()
        except IntegrityError:
            return render(request,"todolist/register.html",{
                "message":"Username Already taken"
            })
        return render(request,"todolist/register.html",{
            "message":"Account created successfully,Please Login."
        })
    else:
        return render(request,"todolist/register.html")

def login(request):
    if request.method=="POST":
        nameinput=request.POST['username']
        passwordinput=request.POST['password']

        user=authenticate(request,username=nameinput,password=passwordinput)
        if user is not None:
            login(request.user)
            return HttpResponseRedirect(reverse("homepage"))
        return render(request,"todolist/login.html",{
            "message":"Invalid Credentials"
        })
    else:
        return render(request,"todolist/login.html")
    
def homepage(request):
    return render(request,"todolist/homepage.html")

def goals(request):
        if request.user.is_authenticated:
            if request.method=="POST":
                input1=request.POST['userGoal']
                input2=request.POST['goaldetails']
                goal=Goals(user=request.user,title=input1,goal=input2)
                goal.save()
                goals = Goals.objects.filter(user=request.user)
                title=Goals.object.filter(user=request.user)
                return render(request, "todolist/goals.html", {
                    "title":title,
                    "goals": goals
                })
        return render(request,"todolist/login.html")


def add(request):
        if request.user.is_authenticated:
            if request.method=="POST":
                input1=request.POST['newtask']
                task=Tasks(user=request.user,tasks=input1)
                task.save()
                tasks = Tasks.objects.filter(user=request.user)
                return render(request, "todolist/goals.html", {
                    "tasks":task
                })
            else:
                return HttpResponseRedirect("add")
        return render(request,"todolist/login.html")




def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

        