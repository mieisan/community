from django.contrib import admin
from django.urls import path, include
from posts import views as post_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # allauth を先にする
    path("accounts/", include("allauth.urls")),
    # その後に自分の accounts
    path("accounts/", include("accounts.urls")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("likes/", include("likes.urls", namespace="likes")),
    path("tags/", include("tags.urls")),
    path("event/", include("events.urls", namespace="events")),   # ← 追加
    path("", post_views.index, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

