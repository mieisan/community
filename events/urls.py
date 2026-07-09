from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.event_calendar, name="calendar"),
    path("list/", views.event_list, name="list"),
    path("create/", views.event_create, name="create"),
    path("<int:pk>/", views.event_detail, name="detail"),
]
