from django.urls import path
from . import views

app_name = "likes"

urlpatterns = [
    path("posts/<int:post_id>/", views.toggle_like, name="toggle_like"),
]
