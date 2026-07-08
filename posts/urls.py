from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),

    path("boards/", views.board_list, name="board_list"),
    path("boards/create/", views.board_create, name="board_create"),
    path("boards/<int:thread_id>/", views.board_detail, name="board_detail"),
    path("boards/<int:thread_id>/reply/", views.reply_create, name="reply_create"),

    path("<int:pk>/", views.post_detail, name="detail"),
]
