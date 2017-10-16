import os
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

GENDER_CHOICES = (
                ('M', 'Male'),
                ('F', 'Female'),
            )


def user_directory_path(instance,filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id,filename)


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    nick_name = models.CharField(max_length=50,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format:'+999999999'.Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=10,validators=[phone_regex],blank=True)
    image = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    has_picture = models.BooleanField(default=False)
    father_name = models.CharField(max_length=50,blank=True)
    whatsapp_no = models.CharField(max_length=10,validators=[phone_regex],blank=True)
    fb_id = models.CharField(max_length=50,blank=True)
    current_address = models.CharField(max_length=250,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name



