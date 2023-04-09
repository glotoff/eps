from import_export import resources
from .models import Player


class BookResource(resources.ModelResource):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'date_of_birth',)
        export_order = ('last_name','first_name','date_of_birth',)
        import_id_fields = ('first_name', 'last_name')
