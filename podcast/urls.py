from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    # Profile URLs
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update-destroy'),

    # PodcastCategory URLs
    path('categories/', PodcastCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', PodcastCategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),

    # PodcastMedia URLs
    path('podcast_media/', PodcastMediaListCreateView.as_view(), name='media-list-create'),
    path('podcast_media/<int:pk>/', PodcastMediaRetrieveUpdateDestroyView.as_view(), name='media-retrieve-update-destroy'),

    # Podcast URLs
    path('podcasts/', PodcastListCreateView.as_view(), name='podcast-list-create'),
    path('podcasts/<int:pk>/', PodcastRetrieveUpdateDestroyView.as_view(), name='podcast-retrieve-update-destroy'),
]
