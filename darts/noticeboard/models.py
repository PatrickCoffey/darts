from django.db import models
from django.utils import timezone

# Create your models here.

class notice(models.Model):
    title = models.CharField(max_length=100)
    post_time = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    text = models.CharField()

    
