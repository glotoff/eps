# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
#from apps.customadmin.views import execute_script

"""
urlpatterns = [
    #good one
    path('admin/', admin.site.urls),          # Django admin route

    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # Leave `Home.Urls` as last the last line
    path("home/", include("apps.home.urls")),
    
    #SG
    path("players/", include("apps.players.urls"))
]
"""
urlpatterns = [
    path("app/admin/", admin.site.urls),          # Django admin route

    path("app/", include("apps.authentication.urls")), # Auth routes - login / register

    # Leave `Home.Urls` as last the last line
    path("app/home/", include("apps.home.urls")),
    
    #SG
    path("app/players/", include("apps.players.urls"))
]
