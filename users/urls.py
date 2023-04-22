from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('api-auth/google/', GoogleLogin.as_view(), name='google_login'),
]
