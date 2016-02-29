from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Video(models.Model):
    """
        A model for holding a video model
    """
    video = models.FileField(upload_to='video/%Y/%m/%d/{}'.format('b4skills_test'), blank=True)
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    textGroup = models.ManyToManyField('VideoText', blank=True)

    def __str__(self):
        if self.description:
            return "{}".format(self.description)
        else:
            return "Video: {}".format(self.pk)

    class Meta:
        ordering = ['-timestamp']


class VideoText(models.Model):
    """
       A model for holding text to display with a video
    """
    parent = models.ForeignKey(Video)
    order = models.IntegerField(default=-1)
    header = models.CharField(max_length=20, blank=True)
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.header:
            return "{}".format(self.header)
        else:
            return "Video Text Object Created On: {}".format(self.timestamp)

    class Meta:
        ordering = ['order']


@receiver(post_save, sender=VideoText)
def add_text_to_video(sender, instance, created=False, **kwargs):
    if created:
        try:
            vid = Video.objects.get(pk=instance.parent.pk)
            vid.textGroup.add(instance)
        except:
            print('Video Text failed to set on Video model')
