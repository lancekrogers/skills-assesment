from django.shortcuts import render

# Create your views here.
from .models import Video


def home(request):
    context = {}
    if Video.objects.all():
        context['video'] = Video.objects.all()[0]
    return render(request, 'skills/home.html', context)
