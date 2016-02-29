from django.conf.urls import url, include

from skills.views import home

urlpatterns = [
    url('^', home, name='home'),
]