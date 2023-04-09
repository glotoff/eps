# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
#from apps.customadmin.views import execute_script

urlpatterns = [
    #good one
    path('admin/', admin.site.urls),          # Django admin route

    #SG
    #path('admin/', admin_site.urls),

    path("", include("apps.authentication.urls")), # Auth routes - login / register

    #path('customadmin/execute-script/', execute_script, name='execute_script'),
    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("home/", include("apps.home.urls")),
    
    #SG
    path("players/", include("apps.players.urls"))
]
