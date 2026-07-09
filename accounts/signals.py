from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount
from .models import Profile


def _get_avatar_url(account):
    data = account.extra_data
    provider = account.provider

    if provider == "github":
        return data.get("avatar_url", "")

    if provider == "google":
        return data.get("picture", "")

    if provider == "discord":
        avatar_hash = data.get("avatar")
        discord_id = data.get("id")
        if avatar_hash and discord_id:
            ext = "gif" if avatar_hash.startswith("a_") else "png"
            return f"https://cdn.discordapp.com/avatars/{discord_id}/{avatar_hash}.{ext}"
        return ""

    if provider == "twitter_oauth2":
        url = data.get("profile_image_url", "")
        return url.replace("_normal", "_400x400") if url else ""

    return ""


@receiver(user_logged_in)
def save_avatar_url_on_login(request, user, **kwargs):
    account = SocialAccount.objects.filter(user=user).first()
    if not account:
        return

    avatar_url = _get_avatar_url(account)
    if not avatar_url:
        return

    profile, _ = Profile.objects.get_or_create(user=user)
    if profile.icon_url != avatar_url:
        profile.icon_url = avatar_url
        profile.save(update_fields=["icon_url"])
