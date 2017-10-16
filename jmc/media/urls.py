from django.conf.urls import url
from media import views


urlpatterns = [
	url(r'^news-and-media$',views.media_page),
	url(r'^image/all$',views.image_page),
]

