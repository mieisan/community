from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


app_name = "accounts"

urlpatterns = [

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("<str:username>/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]
