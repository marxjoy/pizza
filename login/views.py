from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {"message": "Invalid"})
    else:
        return render(request, "users/login.html", {})

    
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out"})


def register_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        if len(username) > 4 and len(password) > 4 and username.isalpha():
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            message = "User " + username + " created."
            return render(request, "users/login.html", {"message": message })
        else:
            message="Invalid"
            return render(request, "users/register.html", {"message": message })
    else:
        return render(request, "users/register.html", {})