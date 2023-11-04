from django.contrib import admin
from .models import Registros, Registros_info
from import_export.admin import ImportExportModelAdmin

#

# Register your models here.
@admin.register(Registros)
class Registros_recursos(ImportExportModelAdmin):
    class Meta:
        model = Registros

@admin.register(Registros_info)
class Registros_recursos(ImportExportModelAdmin):
    class Meta:
        model = Registros_info