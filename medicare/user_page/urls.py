from django.urls import path
from . import views

app_name = "user_page"

urlpatterns = [
    path("", views.user_index_view, name="user_index"),
    path("logout", views.logout_view, name="logout"),
    path("edit_profile", views.edit_profile_view, name="edit_profile"),
    path("edit_profile_func", views.edit_profile_func, name="edit_profile_func"),
    path("edit_profile_success", views.edit_profile_success_view, name="edit_profile_success"),
    path("change_password", views.change_password_view, name="change_password"),
    path("change_password_func", views.change_password_func, name="change_password_func"),
    path("change_password_success", views.change_password_success_view, name="change_password_success")
]