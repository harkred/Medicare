from django.urls import path
from . import views

app_name = "medicine"

urlpatterns = [
    path("add_med", views.add_med_view, name="add_med"),
    path("add_med_func", views.add_med_func, name="add_med_func"),
    path("add_med_success", views.add_med_success_view, name="add_med_success")
]