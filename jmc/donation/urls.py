from django.conf.urls import url
from donation import views


urlpatterns = [
	url(r'^all/$',views.donation_page),
]

