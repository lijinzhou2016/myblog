# coding: utf-8


from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    content = models.TextField(verbose_name="内容", null=True, blank=True)

    def __unicode__(self):
        return self.title
