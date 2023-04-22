from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

from rest_framework import status


# Create your views here.

def home(request):
    return JsonResponse("hey",safe=False)

@api_view(['GET'])
def get_podcasts(request):
    podcasts = Podcast.objects.all()
    serialized_podcasts = PodcastListSerializer(podcasts,many = True) 
    return Response(serialized_podcasts.data)


@api_view(['GET'])
def get_podcast(request,pk):
    try:
        podcast_obj = Podcast.objects.get(id=pk)
        serialized_podcast = PodcastSerializer(podcast_obj,many=False)
        return Response(serialized_podcast.data,status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_podcast_media(request,pk):
    obj = PodcastMedia.objects.get(id=pk)
    print(obj)
    obj = PodcastMediaSerializer(obj,many=False)
    return Response(obj.data)

'''
Audio Duration update -- Add during CRUD operation

from mutagen import File

#Load metadata of the media file
media = File("v1.mp4").info
duration = int(media.length) #Returns the duration in seconds

'''