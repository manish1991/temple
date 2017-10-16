from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from datetime import datetime

from article.models import *


def article_page(request):
    article_list = Article.objects.filter(is_active=True,article_state_id=2)
    if article_list:
        article = article_list.first()
    return render(request,'article/articles.html',locals())


def article_detail(request,article_id,article_url_slug):
	articles = Article.objects.filter(id=article_id,article_state_id=2,is_active=True)
	if articles:
		article = articles.first()
	return render(request,'article/article_detail.html',locals())
