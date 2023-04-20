# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path,include
from apps.players import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.PlayerViewSet)

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('list', views.PlayerListView.as_view(), name='players'),
    path('api/v1/', include((router.urls, '')))
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages')
    #re_path(r'^(?P<page_name>.+)/$', views.pages, name='pages')

]
#+ router.urls
