from django.db import models

from users.models import *
# Create your models here.

class PodcastCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Podcast(models.Model):
    media_choices = (
        ('Audio','Audio'),
        ('Video','Video')
    )

    title = models.CharField(max_length=200, unique=True)
    artists = models.ManyToManyField(Profile)
    description = models.TextField(null=True,blank=True)
    cover_img = models.ImageField(default='cover_img/DSC_0212ps_comp.jpg',upload_to='cover_img/',null=True,blank=True)
    media_type = models.CharField(max_length=50, choices=media_choices)
    categories = models.ManyToManyField(PodcastCategory, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PodcastMedia(models.Model):
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='podcast_media')
    title = models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    # episode_no = models.PositiveBigIntegerField(null=True,blank=True)
    # play_count = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    likes_count = models.PositiveBigIntegerField(null=True,blank=True,default=0)
    created = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='podcast_media/',null=True)
    # media = models.CharField(max_length=200)  #as of now for testing purpose, this is charfield. later change this to file field

    class Meta:
        unique_together = ('podcast', 'title')
        ordering=['-created']

    def __str__(self):
        return f'{self.podcast.title} - {self.title}'


#whenever a user plays a newsong, it should be updated in this last_played field
class PodcastProgress(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    last_played = models.ForeignKey(PodcastMedia,null=True,blank=True, on_delete=models.SET_NULL)
    paused_at = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.profile.user.email


"""each user will have a playlist named Favourites. Podcasts will be added to this whenever like btn is clicked.
If a user likes a entire podcast rather than liking single episodes, then the entire podcast is created as an playlist"""
class Playlist(models.Model):
    name = models.CharField(max_length=250, default='Favourite')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='playlists')
    podcast_medias = models.ManyToManyField("PodcastMedia", blank=True)

    class Meta:
        unique_together = ('profile','name')

    def __str__(self):
        return f'{self.profile.user.email}-{self.name}'
