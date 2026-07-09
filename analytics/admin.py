from django.contrib import admin
from .models import PostView

@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "ip_address", "viewed_at")
