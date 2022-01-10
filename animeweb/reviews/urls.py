from django.urls import path
from . import views

urlpatterns = [
path('', views.reviewsMain, name='reviews-index')

]