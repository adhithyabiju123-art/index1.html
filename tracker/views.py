from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import MoodEntry


@login_required
def tracker(request):
    quote = "Be a rainbow in someone else's cloud."
    author = "Maya Angelou."
    quote = "The only way yo do great work is to love what do you do."
    author = "Steve Jobs."

    if request.method == "POST":
        MoodEntry.objects.create(
            user=request.user,
            rating=request.POST.get("rating"),
            note=request.POST.get("note")
        )
        return redirect("tracker")

    history = MoodEntry.objects.filter(user=request.user).order_by("-data_created")

    stats = (
        MoodEntry.objects.filter(user=request.user)
        .values("rating")
        .annotate(total=Count("rating"))
        .order_by("rating")
    )

    context = {
        "quotes": quote,
        "author": author,
        "choices": MoodEntry.MOOD_CHOICES,
        "history": history,
        "stats": stats,
    }

    return render(request, "tracker/trck.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')