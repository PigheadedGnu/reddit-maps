from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget

from map.models import Map, Submission
from project import sqlite_fields


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    pass


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        sqlite_fields.JSONField: {'widget': JSONEditorWidget},
    }
