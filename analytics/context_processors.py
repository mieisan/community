from django.db.models import Count
from posts.models import Post

def sidebar(request):
    latest_posts = Post.objects.order_by("-created_at")[:5]

    popular_posts = (
        Post.objects
        .annotate(view_count=Count("views"))
        .order_by("-view_count")[:5]
    )

    liked_posts = Post.objects.order_by("-created_at")[:5]  # 仮

    return {
        "latest_posts": latest_posts,
        "popular_posts": popular_posts,
        "liked_posts": liked_posts,
    }
