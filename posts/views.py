import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from analytics.models import PostView

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    return request.META.get("REMOTE_ADDR")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    cookie_id = request.COOKIES.get("visitor_id")
    if not cookie_id:
        cookie_id = str(uuid.uuid4())

    if request.user.is_authenticated:
        PostView.objects.get_or_create(
            post=post,
            user=request.user,
        )
    else:
        PostView.objects.get_or_create(
            post=post,
            cookie_id=cookie_id,
            defaults={
                "ip_address": get_client_ip(request),
                "user_agent": request.META.get("HTTP_USER_AGENT", ""),
                "referer": request.META.get("HTTP_REFERER", ""),
            },
        )

    response = render(request, "posts/detail.html", {"post": post})
    response.set_cookie("visitor_id", cookie_id, max_age=60 * 60 * 24 * 365)

    return response

@login_required
def create(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('/')

    else:
        form = PostForm()

    return render(
        request,
        'posts/create.html',
        {'form': form}
    )

