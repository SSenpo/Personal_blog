from django.urls import path
from . import views

urlpatterns = [
    # path("logout", views.about_page, name="logout"),
    # path("profile", views.about_page, name="profile"),
    path("about", views.about_page, name="blog-about"),
    path("", views.PostListView.as_view(), name="blog-home"),
    path("home", views.PostListView.as_view(), name="blog-home"),
    path("post/new", views.PostCreateView.as_view(), name="blog-new"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="blog-detail"),
    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="blog-update"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="blog-delete"),
]
