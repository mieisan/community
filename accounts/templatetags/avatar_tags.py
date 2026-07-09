from django import template

register = template.Library()

DEFAULT_AVATAR = "/static/img/default_avatar.png"


@register.simple_tag
def avatar_url(user):
    profile = getattr(user, "profile", None)
    if profile is None:
        return DEFAULT_AVATAR
    if profile.icon_url:
        return profile.icon_url
    if profile.icon:
        return profile.icon.url
    return DEFAULT_AVATAR
