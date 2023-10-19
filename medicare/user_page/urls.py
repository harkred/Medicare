from django.urls import path
from . import views

app_name = "user_page"

urlpatterns = [
    path("", views.user_index_view, name="user_index"),
    path("logout", views.logout_view, name="logout")
]