from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from django_musicbrainz_connector import models


class DjangoMusicBrainzConnectorModelAdmin(admin.ModelAdmin):
    """Subclass of `admin.ModelAdmin` that prevents adding, editing or deleting objects in the Admin interface."""

    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


@admin.register(models.ArtistCredit)
class ArtistCreditAdmin(DjangoMusicBrainzConnectorModelAdmin):
    pass


@admin.register(models.Link)
class LinkAdmin(DjangoMusicBrainzConnectorModelAdmin):
    pass


@admin.register(models.LinkType)
class LinkTypeAdmin(DjangoMusicBrainzConnectorModelAdmin):
    list_display = ["name", "entity_type0", "entity_type1", "description"]


@admin.register(models.Recording)
class RecordingAdmin(DjangoMusicBrainzConnectorModelAdmin):
    pass


@admin.register(models.RecordingWorkLink)
class RecordingWorkLinkAdmin(DjangoMusicBrainzConnectorModelAdmin):
    list_display = ["id", "link_type", "recording", "work"]


@admin.register(models.Work)
class WorkAdmin(DjangoMusicBrainzConnectorModelAdmin):
    pass


@admin.register(models.WorkType)
class WorkTypeAdmin(DjangoMusicBrainzConnectorModelAdmin):
    pass
