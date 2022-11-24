from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Articel(models.Model):
    title = models.CharField(max_length=100)
    slog = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(default="default.jpg", blank = True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # Return in Admin title alternative object
    def __str__(self):
        return self.title
    
    def snippet(self):
        if (len(self.body) > 50):
            return self.body[:50] + "..."
        else:
            return self.body