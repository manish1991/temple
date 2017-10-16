from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from datetime import datetime
from media.models import *


def image_page(request):
    image_list = Image.objects.filter(is_active=True)
    video_list = Video.objects.filter(is_active=True)
    print('@@@', image_list)
    return render(request,'media/galleries.html',locals())


def media_page(request):
    video_list = Video.objects.filter(is_active=True)
    print('@@@', video_list)
    return render(request,'media/media.html',locals())