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

def edit_med_view(request):
    medicines = Medicine.objects.filter(med_id=request.user)
    context = {
        "medicines": medicines
    }
    return render(request, "edit_med.html", context)

def edit_med_func(request):
    if request.method == "POST":
        Medicine.objects.filter(id=request.POST["mid"], med_id=request.user).update(
            med_id=request.user,
            med_name=request.POST["med_name"],
            med_dosage=request.POST["med_dosage"],
            med_frequency=request.POST["med_frequency"]
        )
        return redirect("medicine:edit_med_success")
    
def edit_med_success_view(request):
    return render(request, "edit_med_success.html")