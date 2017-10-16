from django.db import models
from base.models import AuditModel

# Create your models here.


class Image(AuditModel):
    title = models.CharField(max_length=255,blank=True)
    image_path = models.FileField(upload_to='images/',null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Video(AuditModel):
    video_link = models.CharField(max_length=255,blank=True)
    is_active = models.BooleanField(default=True)