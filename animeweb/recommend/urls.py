from django.urls import path
from . import views
from .views import AnimeListView, AnimeDetailView
from django.conf import settings
from django.conf.urls.static import static

# Url configuration
urlpatterns = [
    path('', views.index, name='recommend-index'),
    path('about/', views.about, name='recommend-about'),
    #path('results/', views.results, name='recommend-results'),
    path('results/', views.recResults, name='recommend-results'),
    path('anime/', AnimeListView.as_view(), name='all-anime'),
    path('add_to_list/', views.all_anime, name='add-to-list'),
    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #only add on when in debug mode