from django.urls import path
from .views import *

app_name = 'cam'

urlpatterns = [
  path('', show_cctv, name='index'),
  path('livecam/', livecam, name='livecam'),
]
