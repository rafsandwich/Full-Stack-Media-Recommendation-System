from django.contrib import admin
from .models import Anime, Tag, Review

# Register your models here.
admin.site.register(Anime)
admin.site.register(Tag)
admin.site.register(Review)