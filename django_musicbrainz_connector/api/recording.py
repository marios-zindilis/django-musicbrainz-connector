import uuid
from typing import Literal

from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import Recording


class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = "__all__"


def _get_recording_identifier_type(identifier: str | int) -> Literal["gid", "id"]:
    """
    A Recording can be identified either by its ID or its GID.
    """
    try:
        uuid.UUID(identifier)
    except (ValueError, AttributeError):
        return "id"
    else:
        return "gid"


class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by any unique identifier for a Work,
        either the MusicBrainz ID (an integer), or the GID (a UUID). Call with something like:

            GET /api/recordings/1234/
        """
        pk = self.kwargs["pk"]
        pk_type = _get_recording_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return self.serializer_class.Meta.model.objects.get(**params)
        except self.serializer_class.Meta.model.DoesNotExist:
            raise NotFound
