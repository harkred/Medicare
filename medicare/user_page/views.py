from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def user_index_view(request):
    context = {
        "name": request.user.name
    }
    return render(request, "user_index.html", context)

def logout_view(request):
    logout(request)
    return redirect("home:index")