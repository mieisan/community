from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added, social_account_updated
from .models import Profile


def _get_avatar_url(sociallogin):
    account = sociallogin.account
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


@receiver(social_account_added)
@receiver(social_account_updated)
def save_avatar_url(request, sociallogin, **kwargs):
    avatar_url = _get_avatar_url(sociallogin)
    if not avatar_url:
        return

    user = sociallogin.user
    profile, _ = Profile.objects.get_or_create(user=user)
    if profile.icon_url != avatar_url:
        profile.icon_url = avatar_url
        profile.save(update_fields=["icon_url"])
