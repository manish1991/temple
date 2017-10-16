from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import datetime

from account.services import *
from account.models import *
from account.forms import *
# from batch.services import activate_answer_set_service

# from organization.models import UserOrganizationMapping


# Create your views here.

def home_page(request):
    return render(request,'account/home.html',{})


def committee_member(request):
    user_profiles = UserProfile.objects.filter(is_active=True)
    user_profile_list = list(user_profiles) + list(user_profiles) + list(user_profiles) +\
                        list(user_profiles) + list(user_profiles) + list(user_profiles) + \
                        list(user_profiles) + list(user_profiles) + list(user_profiles) + \
                        list(user_profiles) + list(user_profiles) + list(user_profiles) +\
                        list(user_profiles) + list(user_profiles) + list(user_profiles)
    print('$$$',user_profiles)
    return render(request,'account/committee_member.html',locals())    