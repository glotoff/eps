# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.players import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('list', views.PlayerListView.as_view(), name='players'),
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages')
    #re_path(r'^(?P<page_name>.+)/$', views.pages, name='pages')

]
