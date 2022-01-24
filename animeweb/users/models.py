from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio_desc = 
    profile_pic = models.ImageField(default='defaultUser.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        #prev_img= Profile.objects.get(id=self.id)
        super().save(*args, **kwargs)

        #resizing larger images to improve website performance
        img = Image.open(self.profile_pic.path)

        #if prev_img!=self.profile_pic:
        #    prev_img.profile_pic.delete(save=False)

        if img.height> 350 or img.width >350:
            new_size = (350, 350)
            img.thumbnail(new_size)
            img.save(self.profile_pic.path)