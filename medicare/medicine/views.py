from django.shortcuts import render, redirect
from .models import Medicine
# Create your views here.
def add_med_view(request):
    return render(request, "add_med.html")

def add_med_func(request):
    if request.method == "POST":
        Medicine.objects.create(
            med_id=request.user,
            med_name=request.POST["med_name"],
            med_dosage=request.POST["med_dosage"],
            med_frequency=request.POST["med_frequency"]
        )
        return redirect("medicine:add_med_success")
    
def add_med_success_view(request):
    return render(request, "add_med_success.html")