from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from medicine.models import Medicine
from users.models import CustomUser

# Create your views here.
def user_index_view(request):
    context = {
        "name": request.user.name,
        "medicines": Medicine.objects.filter(med_id=request.user)
    }
    return render(request, "user_index.html", context)

def logout_view(request):
    logout(request)
    return redirect("home:index")

def edit_profile_view(request):
    context = {
        "email": request.user.email,
        "name": request.user.name,
        "err": None
    }
    return render(request, "edit_user.html", context)

def edit_profile_func(request):
    if request.method == "POST":
        try:
            CustomUser.objects.filter(id=request.user.id).update(
                email=request.POST["email"],
                name = request.POST["name"]
            )
        except Exception:
            context = {
                "email": request.user.email,
                "name": request.user.name,
                "err": "Such Email already in use!!"
            }
            redirect("user_page:edit_profile")
            return render(request, "edit_user.html", context)
        return redirect("user_page:edit_profile_success")

def edit_profile_success_view(request):
    return render(request, "edit_user_success.html")

def change_password_view(request):
    context = {
        "err": None
    }
    return render(request, "change_password.html", context)

def change_password_func(request):
    if request.method == "POST":
        if not check_password(request.POST['old_password'], request.user.password):
            context = {
                "err": "Your old password is incorrect"
            }
            return render(request, "change_password.html", context)
        else:
            request.user.set_password(request.POST["new_password"])
            request.user.save()
            return redirect("user_page:change_password_success")

def change_password_success_view(request):
    return render(request, "change_password_success.html")