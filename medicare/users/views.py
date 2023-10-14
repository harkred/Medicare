from django.shortcuts import render

# Create your views here.
def join_us(request):
    context = {

    }
    return render(request, "users/join_us.html", context)