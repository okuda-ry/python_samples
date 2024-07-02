from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Link
from .form import LinkForm, ProfileForm
from django.contrib.auth.models import User


def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get_or_create(user=user)[0]
    links = Link.objects.filter(user=user).order_by("order")
    return render(request, "links/profile.html", {"profile": profile, "links": links})


@login_required
def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect("profile", username=request.user.username)
    else:
        form = LinkForm()
    return render(request, "links/add_link.html", {"form": form})


@login_required
def edit_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, "links/edit_profile.html", {"form": form})


def home(request):
    if request.user.is_authenticated:
        return redirect("profile", username=request.user.username)
    return render(request, "links/home.html")


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "links/signup.html", {"form": form})
