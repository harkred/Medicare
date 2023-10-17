from django.shortcuts import render, redirect
from users.models import CustomUser
# Create your views here.
def register_view(request):
    if request.method == "POST":
        CustomUser.objects.create_user(email=request.POST["email"], password=request.POST["password"], name=request.POST["name"])
        return render(request, "register_success.html")
    return redirect("home:index")

def login_view(request):
    pass