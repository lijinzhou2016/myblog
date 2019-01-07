from django.contrib import admin

# Register your models here.
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content")


admin.site.register(Article, ArticleAdmin)