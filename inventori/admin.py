from django.contrib import admin
from .models import Pembekal, Stok, Inventori
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Pembekal)
admin.site.register(Stok)

class InventoriResource(resources.ModelResource):

    class Meta:
        model = Inventori
        fields = ('inventori', 'harga', 'kuantiti',)

@admin.register(Inventori)
class InventoriAdmin(ImportExportModelAdmin):
    pass