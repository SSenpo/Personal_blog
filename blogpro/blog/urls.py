from django.urls import path
from . import views

urlpatterns = [
    path("logout", views.about_page, name="logout"),
    path("profile", views.about_page, name="profile"),
    path("new", views.about_page, name="blog-new"),
    path("about", views.about_page, name="blog-about"),
    path("home", views.home_page, name="blog-home"),
    path("", views.home_page, name=""),
]
