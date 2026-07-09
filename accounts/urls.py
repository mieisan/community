from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from allauth.socialaccount.models import SocialAccount

app_name = "accounts"

def get_avatar_url(user):
    """ログイン中のソーシャルアカウントからアバターURLを取得する"""
    account = SocialAccount.objects.filter(user=user).first()
    if not account:
        return None

    data = account.extra_data
    provider = account.provider

    if provider == "github":
        return data.get("avatar_url")

    if provider == "google":
        return data.get("picture")

    if provider == "discord":
        avatar_hash = data.get("avatar")
        discord_id = data.get("id")
        if avatar_hash and discord_id:
            ext = "gif" if avatar_hash.startswith("a_") else "png"
            return f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar_hash}.{ext}"
        return None

    if provider == "twitter_oauth2":
        # デフォルトは低解像度(_normal)なので高解像度に置換
        url = data.get("profile_image_url")
        if url:
            return url.replace("_normal", "_400x400")
        return None

    return None

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("<str:username>/", views.profile, name="profile"),
]
