from django.contrib import admin

from . import resources
from .models import Player
from import_export.admin import ImportExportModelAdmin


class PlayerAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name",)
    search_fields = ('first_name', 'last_name')
    list_filter = ('date_of_birth',)
    resource_class = resources.BookResource

admin.site.register(Player, PlayerAdmin)