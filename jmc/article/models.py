from django.db import models
from base.models import AuditModel
from account.models import UserProfile
from media.models import Image

# Create your models here.


class ArticleTopic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class ArticleState(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Article(AuditModel):
    title = models.CharField(db_index=True,max_length=255)
    snippet_text = models.TextField()
    url = models.CharField(max_length=255,blank=True)
    url_slug = models.CharField(max_length=255,blank=True)
    cover_image = models.ForeignKey(Image)
    body = models.TextField(blank=True)
    author = models.ForeignKey(UserProfile,null=True,default=None)
    video_link = models.CharField(max_length=255,blank=True)
    article_state = models.ForeignKey(ArticleState,null=True)
    is_active = models.BooleanField(default=True)
    search_text = models.CharField(max_length=255,blank=True)
    publish_time = models.DateTimeField(null=True,blank=True)
    api_calls = models.IntegerField(blank=True,null=True,default=0)

    def __unicode__(self):
        return self.title