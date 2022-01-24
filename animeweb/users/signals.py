from django.db.models.signals import post_save #signal fired after object saved
from django.contrib.auth.models import User #sender, sends the signal
from django.dispatch import receiver 
from .models import Profile

#when a user is saved, then send this signal received by createProfile function
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    #if user was created
    if created:
        #create profile object with user = instance of user that was created
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()