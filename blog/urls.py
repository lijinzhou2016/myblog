#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Time    : 2018/12/2 7:49 PM
# @Author  : LiJinzhou
# @File    : urls.py


from django.conf.urls import url, include
from django.contrib import admin
import views


urlpatterns = [
    url(r'^list/', views.index),
    url(r'^article/(?P<article_id>\d+)$', views.article_page, name="article_page"),
    url(r'^edit/(?P<article_id>\d+)$', views.edit_page, name="edit_page"),
    url(r'^edit/action/$', views.edit_action, name="edit_action"),
]