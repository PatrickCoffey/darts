from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    post_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField(unique=False)    
    
    @models.permalink
    def get_absolute_url(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Notice, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title