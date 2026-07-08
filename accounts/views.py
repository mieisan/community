from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from posts.models import Post
from .models import Profile
from .forms import ProfileForm


def profile(request, username):
    user = get_object_or_404(User, username=username)

    profile, created = Profile.objects.get_or_create(user=user)

    posts = Post.objects.filter(user=user).order_by("-created_at")

    return render(
        request,
        "accounts/profile.html",
        {
            "profile_user": user,
            "profile": profile,
            "posts": posts,
        }
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    else:
        form = UserCreationForm()

    return render(
        request,
        "accounts/signup.html",
        {"form": form}
    )


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("accounts:profile", username=request.user.username)

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form}
    )
