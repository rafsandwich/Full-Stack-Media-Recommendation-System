from django.urls import path
from . import views
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, UserReviewListView

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews-index'),
  # path('', views.reviewsMain, name='reviews-index' 
    path('<int:pk>/', ReviewDetailView.as_view(), name='reviews-detail'),
    path('new/', ReviewCreateView.as_view(), name='reviews-create'), #primary key for unique review pages
    path('<int:pk>/update/', ReviewUpdateView.as_view(), name='reviews-update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='reviews-delete'),
    path('user/<str:username>/', UserReviewListView.as_view(), name='user-reviews'),
]