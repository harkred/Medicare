from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register", views.register_func, name="register"),
    path("login", views.login_func, name="login")
]