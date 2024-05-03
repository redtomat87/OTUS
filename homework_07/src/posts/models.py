from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

