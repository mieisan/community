from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField("タイトル", max_length=200)
    description = models.TextField("説明", blank=True)
    start_datetime = models.DateTimeField("開始日時")
    end_datetime = models.DateTimeField("終了日時", null=True, blank=True)
    location = models.CharField("開催場所", max_length=255, blank=True)
    fee = models.CharField("参加費", max_length=100, blank=True)
    capacity = models.PositiveIntegerField("定員", null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_datetime"]

    def __str__(self):
        return self.title
