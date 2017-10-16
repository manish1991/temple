from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from datetime import datetime

from donation.models import *


def donation_page(request):
    donation_list = Donation.objects.filter(is_active=True)
    return render(request,'donation/donations.html',locals())

