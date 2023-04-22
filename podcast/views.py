from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.

def home(request):
    return JsonResponse("hey",safe=False)

# Podcast views
class PodcastList(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastListSerializer
    permission_classes = [IsAuthenticated]

class PodcastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [IsAuthenticated]

# PodcastMedia views
class PodcastMediaList(generics.ListCreateAPIView):
    queryset = PodcastMedia.objects.all()
    serializer_class = PodcastMediaSerializer
    permission_classes = [IsAuthenticated]

class PodcastMediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PodcastMedia.objects.all()
    serializer_class = PodcastMediaSerializer
    permission_classes = [IsAuthenticated]

'''
Audio Duration update -- Add during CRUD operation

from mutagen import File

#Load metadata of the media file
media = File("v1.mp4").info
duration = int(media.length) #Returns the duration in seconds

'''