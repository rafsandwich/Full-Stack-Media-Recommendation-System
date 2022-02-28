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

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Anime(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=7)
    episodes = models.IntegerField()
    status = models.CharField(max_length=10)
    year = models.IntegerField()
    picture = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

#Anime(title=anime['title'], type=anime['type'], episodes=anime['episodes'],
#  status=anime['status'], year=anime['year'], picture=anime['picture'], tags=anime['tags'])
