from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from django_musicbrainz_connector.models import WorkType


class DjangoMusicBrainzConnectorModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False


@admin.register(WorkType)
class WorkTypeAdmin(DjangoMusicBrainzConnectorModelAdmin):
    pass
