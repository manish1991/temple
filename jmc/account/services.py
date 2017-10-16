from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from account.models import UserProfile


def reset_password_service(request,email):
    users = UserProfile.objects.filter(user__email=email)
    if users:
        user = users.first()
        reset_password_url = 'http://' + str(request.META['HTTP_HOST']) + '/user/'+\
                                                         str(user.id)+'/reset-password/'
        subject = 'Reset your password'
        
        html_content = render_to_string("account/forgot_password_content.html", 
                                       {'reset_password_url':reset_password_url})
        text_content = strip_tags(html_content)
        from_mail = 'shaibig.cdx@gmail.com'
        to_mail = [email]
        msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        user.is_previously_logged_in = False
        return 
    else:
        return 'Email id not registered.'


def edit_profile_page_service(first_name,last_name,email,gender,phone_no,user,user_profile):
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.save()
    user_profile.gender=gender
    user_profile.phone_no=phone_no
    user_profile.save()