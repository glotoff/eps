from django.contrib import admin

from . import resources
from .models import Player
from .models import PlayerClub
from .models import PlayerTournament

from import_export.admin import ImportExportModelAdmin


class ClubInline(admin.TabularInline):
    model = Player.clubs.through


@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ('first_name', 'last_name')
    list_filter = ('date_of_birth',)
    inlines = [
        ClubInline,
    ]
#    resource_class = resources.BookResource

# admin.site.register(PlayerClub)
# admin.site.register(PlayerTournament)
# admin.site.register(Player, PlayerAdmin)
