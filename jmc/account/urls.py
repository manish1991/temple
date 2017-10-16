

from django.conf.urls import url
from account import views


urlpatterns = [
	url(r'^home/$',views.home_page),
    url(r'^committee-member/$',views.committee_member),
    ]