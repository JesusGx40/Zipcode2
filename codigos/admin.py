from django.contrib import admin
from .models import  Registros_info
from import_export.admin import ImportExportModelAdmin


@admin.register(Registros_info)
class Registros_recursos(ImportExportModelAdmin):
    class Meta:
        model = Registros_info