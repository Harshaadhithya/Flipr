from rest_framework import serializers

from .models import *
from users.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastCategory
        fields = ['name']


class PodcastListSerializer(serializers.ModelSerializer):
    artists = ProfileSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Podcast
        fields = '__all__'


class PodcastMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastMedia
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    artists = ProfileSerializer(many=True)
    categories = CategorySerializer(many=True)

    podcast_medias = serializers.SerializerMethodField()
    
    class Meta:
        model = Podcast
        fields = '__all__'

    def get_podcast_medias(self,obj):
        podcast_medias = obj.podcast_media.all()
        serialized_podcast_medias = PodcastMediaSerializer(podcast_medias,many=True)
        return serialized_podcast_medias.data





