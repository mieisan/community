from django.shortcuts import get_object_or_404, render
from .models import Tag

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.all()

    return render(request, "tags/tag_detail.html", {
        "tag": tag,
        "posts": posts,
    })
