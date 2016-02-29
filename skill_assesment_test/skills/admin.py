from django.contrib import admin

from useful_function import register
from .models import VideoText, Video

# Register your models here.
sat = [Video, VideoText]
register(sat)
