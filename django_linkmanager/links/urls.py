from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<str:username>/", views.profile_view, name="profile"),
    path("add-link/", views.add_link, name="add_link"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="links/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("signup/", views.signup, name="signup"),
]
