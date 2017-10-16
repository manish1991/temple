from django.conf.urls import url
from article import views


urlpatterns = [
	url(r'^all/$',views.article_page),
	url(r'^(?P<article_id>\d+)/(?P<article_url_slug>\w+)/$', views.article_detail),
]

# url(r'^committee-member/$',views.committee_member),