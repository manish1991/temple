from django.contrib import admin
from article.models import *

# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display = ('title','snippet_text','url','url_slug','body','author','video_link',
    				'article_state','is_active','search_text')
    search_fields = ('title','search_text')
    list_filter = ('created_by',)


admin.site.register(Article,AdminArticle)
admin.site.register(ArticleTopic)
admin.site.register(ArticleState)
admin.site.register(ArticleCategory)