from django.urls import path
from . import views

app_name = "medicine"

urlpatterns = [
    path("add_med", views.add_med_view, name="add_med"),
    path("add_med_func", views.add_med_func, name="add_med_func"),
    path("add_med_success", views.add_med_success_view, name="add_med_success"),
    path("edit_med", views.edit_med_view, name="edit_med"),
    path("edit_med_func", views.edit_med_func, name="edit_med_func"),
    path("edit_med_success", views.edit_med_success_view, name="edit_med_success"),
    path("del_med", views.del_med_view, name="del_med"),
    path("del_med_func", views.del_med_func, name="del_med_func"),
    path("del_med_success", views.del_med_success_view, name="del_med_success")
]