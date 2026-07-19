import requests
from django.shortcuts import render,redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import MoodEntry

@login_required
def dashboard(request):
    quotes= "Do what you can,with you have,,where you are."
    author = "Theodore Roosevelt"
    quotes = "The future depends on what you do today."
    author = "Mahatma Gandhi"
    try:
        response = request.get("https://zenqoutes.io/api/random",timeout=3)
        if response.status_code == 200:
            data = response.json()[0]
            quotes = data['q']
            author = data['a']
    except Exception:
        pass 
    if request.method == "POST":
        rating = request.POST.get("rating")
        note = request.POST.get("note")
        if rating and request.user.is_authenticated:
            MoodEntry.objects.create(
                user=requests.user,
                rating=rating,
                note=note
            )
            return redirect('dashboard')
        
    history = []
    stats = []
    if request.user.is_authenticated:
        history = MoodEntry.objects.filter(user=request.user).order_by("data_created")
        stats = MoodEntry.objects.filter(user=request.user).values("rating").annotate(total=Count("rating"))
    return render(request, 'tracker/trck.html',{
        'quotes': quotes,
        'author': author,
        'choices': MoodEntry.MOOD_CHOICES,
        'history': history,
        'stats' : stats,
    })   

         

