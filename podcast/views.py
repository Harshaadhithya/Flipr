from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.

def index(request):
    return JsonResponse("Hello World!",safe=False)

# Create API views for Profile model
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

# Create API views for PodcastCategory model
class PodcastCategoryListCreateView(generics.ListCreateAPIView):
    queryset = PodcastCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class PodcastCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PodcastCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Create API views for PodcastMedia model
class PodcastMediaListCreateView(generics.ListCreateAPIView):
    queryset = PodcastMedia.objects.all()
    serializer_class = PodcastMediaSerializer
    permission_classes = [IsAuthenticated]

class PodcastMediaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PodcastMedia.objects.all()
    serializer_class = PodcastMediaSerializer
    permission_classes = [IsAuthenticated]

# Create API views for Podcast model
class PodcastListCreateView(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastListSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PodcastRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def put(self, request, *args, **kwargs):
        podcast = self.get_object()
        serializer = self.serializer_class(podcast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Audio Duration update -- Add during CRUD operation

from mutagen import File

#Load metadata of the media file
media = File("v1.mp4").info
duration = int(media.length) #Returns the duration in seconds

'''