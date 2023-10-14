from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.join_us, name="join_us")
]