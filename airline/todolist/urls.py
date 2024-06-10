from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("homepage",views.homepage,name="homepage"),
    path("goals",views.goals,name="goals"),
    path("add",views.add,name="add"),
    path("logout",views.logout,name="logout")
]