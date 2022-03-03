from . import views
from django.urls import path

urlpatterns=[
    path("remove_from_list/", views.removeFromUserList)
]