from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportMixin
from djangoql.admin import DjangoQLSearchMixin

from .models import Application


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = ('name', 'phone', 'message', 'date_create', 'is_accept', 'date_accept',)


@admin.register(Application)
class ApplicationAdmin(ImportExportMixin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'date_create', 'is_accept', 'date_accept', 'id']
    list_filter = ['date_create']
    ordering = ['-date_create', 'name']
    resource_classes = (ApplicationResource, )
    list_editable = ['is_accept']
