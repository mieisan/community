from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post
from .models import Like


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post,
    )

    if not created:
        like.delete()

    return redirect("/")
