from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    icon = models.ImageField(upload_to="profile_icons/", blank=True, null=True)
    icon_url = models.URLField(blank=True)   # ←追加

    def __str__(self):
        return self.user.username
