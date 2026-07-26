from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        (1, '😥 Awful'),
        (2, '☹️ Meh'),
        (3, '😑 okey'),
        (4, '😊 Good'),
        (5, '🤩 Amazing'),
                ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rating = models.IntegerField(choices=MOOD_CHOICES)
    note = models.TextField(blank=True,null=True)
    data_created = models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return f"{self.data_created.strftime('%Y-%m-%d')}-{self.get_rating_display()}"
    
