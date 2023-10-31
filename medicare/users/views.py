from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth import login, authenticate
from django.urls import reverse

# Create your views here.
def register_func(request):
    if request.method == "POST":
        try:
            CustomUser.objects.create_user(email=request.POST["email"], password=request.POST["password"], name=request.POST["name"])
            return render(request, "register_success.html")
        except Exception:
            return render(request, "index.html", {"err": "Email already exists"})
    return redirect("home:index")

def login_func(request):
    if request.method == "POST":
        user = authenticate(email=request.POST["email"], password=request.POST["password"])

        if user is not None:
            login(request, user)
            return redirect("user_page:user_index")
    return render(request, "index.html", {"err": "Invalid username/password"})