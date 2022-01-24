from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#class User(models.Model):
#    username = models.CharField(max_length=12)
#    password = models.CharField(max_length=255)

class Review(models.Model):
    head = models.CharField(max_length=80)
    body = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, choose what happens to reviews

    def __str__(self):
        return self.head #for visiblity in cmd prompt

    def get_absolute_url(self):
        return reverse('reviews-detail', kwargs={'pk': self.pk})

#class Anime(models.Model):
