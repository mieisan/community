from django.conf import settings
from django.db import models
from posts.models import Post


class PostView(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="views",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    cookie_id = models.CharField(max_length=64, null=True, blank=True)
    user_agent = models.TextField(blank=True)
    referer = models.URLField(blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["post"]),
            models.Index(fields=["user"]),
            models.Index(fields=["ip_address"]),
            models.Index(fields=["cookie_id"]),
            models.Index(fields=["viewed_at"]),
        ]

    def __str__(self):
        return f"{self.post_id} viewed by {self.user_id or self.cookie_id or self.ip_address}"
