from django.urls import path
from . import views

# Url configuration
urlpatterns = [
    path('', views.index, name='recommend-index'),
    path('about/', views.about, name='recommend-about'),

]