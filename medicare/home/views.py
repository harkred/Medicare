from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {
        "err": None
    }
    return render(request, "index.html", context)