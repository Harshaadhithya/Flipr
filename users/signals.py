from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import Profile

@receiver(user_signed_up)
def create_profile(sender, request, user, **kwargs):
    if not hasattr(user, 'profile'):
        profile = Profile.objects.create(
            user=user,
            role='normal_user' #Default role
        )
        user.profile = profile
        #Assign roles based on mail id
        # if user.email.endswith('.admin@podcast.com'):
        #     profile.role = 'admin'
        # elif user.email.endswith('.artist@podcast.com'):
        #     profile.role = 'artist'
        user.save()