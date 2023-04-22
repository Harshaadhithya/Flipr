from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('podcasts/', PodcastList.as_view(), name='podcast-list'),
    path('podcasts/<int:pk>/', PodcastDetail.as_view(), name='podcast-detail'),
    path('podcastmedia/', PodcastMediaList.as_view(), name='podcastmedia-list'),
    path('podcastmedia/<int:pk>/', PodcastMediaDetail.as_view(), name='podcastmedia-detail'),
]
