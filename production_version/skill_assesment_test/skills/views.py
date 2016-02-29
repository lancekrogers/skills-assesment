from django.shortcuts import render

# Create your views here.
from .models import Video


def home(request):
    context = {}
    try:
        if Video.objects.all():
            context['video'] = Video.objects.all()[0]
    except:
        print("An error occured in your views")
    return render(request, 'skills/home.html', context)
