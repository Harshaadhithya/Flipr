from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('get_podcasts/',get_podcasts,name='get_podcasts'),
    path('get_podcasts/<str:pk>/',get_podcast, name='get_podcast'),
    path('get_podcast_media/<str:pk>/',get_podcast_media,name='get_podcast_media')
]
