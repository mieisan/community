from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models import Post


def profile(request, username):
    user = get_object_or_404(User, username=username)

    profile, created = Profile.objects.get_or_create(
        user=user
    )

    posts = Post.objects.filter(
        user=user
    ).order_by('-created_at')

    return render(
        request,
        "accounts/profile.html",
        {
            "profile_user": user,
            "profile": user.profile,
            "posts": posts,
        }
    )

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')

    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/signup.html",
        {"form": form}
    )


    return render(
        request,
        "accounts/profile.html",
        {
            "profile_user": user,
            "profile": profile,
            "posts": posts,
        }
    )
