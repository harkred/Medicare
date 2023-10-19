from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register_func(request):
    if request.method == "POST":
        CustomUser.objects.create_user(email=request.POST["email"], password=request.POST["password"], name=request.POST["name"])
        return render(request, "register_success.html")
    return redirect("home:index")

def login_func(request):
    if request.method == "POST":
        user = authenticate(email=request.POST["email"], password=request.POST["password"])

        if user is not None:
            login(request, user)
            return redirect("user_page:user_index")