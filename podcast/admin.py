from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PodcastCategory)
admin.site.register(Podcast)
admin.site.register(PodcastMedia)
admin.site.register(PodcastProgress)
admin.site.register(Playlist)

