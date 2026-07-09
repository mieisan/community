# tags/urls.py
from django.urls import path
from . import views

app_name = "tags"

urlpatterns = [
    path("<str:slug>/", views.tag_detail, name="detail"),
]
