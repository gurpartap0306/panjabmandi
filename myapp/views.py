from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import User

def index(request):
    return render(request,"myapp/index.html")

def login_view(request):
    if request.method == "POST":

        #Attempt to sign user in
        username = request.POST["username"]
        password =request.POST["password"]
        user = authenticate(request,username=username,password=password)

        #check if authentication successful
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"myapp/login.html",{
                "message":"Invalid username and/or password."
            })
    else:
        return render(request,"myapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        #Ensure password matches confirmation
        password = request.POST["password"]
        confirmation=request.POST["confirmation"]
        if password != confirmation:
            return render(request,"myapp/register.html",{
            "message":"passords must match."
            })

        #attemp to create new user
        try:
<<<<<<< HEAD
            user = User.object.create_user(username,email,password)
=======
            user = User.objects.create_user(username,email,password)
>>>>>>> 56c4f79f8128b23b40f4bf7a114e488618908a1c
            user.save()
        except IntegrityError:
            return render(request,"myapp.register.html",{
            "message": "Username already taken."
            })
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"myapp/register.html")
