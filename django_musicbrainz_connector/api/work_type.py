import uuid
from typing import Literal

from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.models import WorkType


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = "__all__"


def _get_work_type_identifier_type(identifier: str | int) -> Literal["gid", "name", "id"]:
    try:
        uuid.UUID(identifier)
    except (ValueError, AttributeError):
        pass
    else:
        return "gid"
    try:
        int(identifier)
    except ValueError:
        return "name"
    else:
        return "id"


class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    http_method_names = ["get"]

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by any unique identifier for a Work
        Type, either the MusicBrainz ID (an integer), or the GID (a UUID), or the name (a string). Call with something
        like:

            GET /api/work-types/Musical/
        """
        pk = self.kwargs["pk"]
        pk_type = _get_work_type_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return self.serializer_class.Meta.model.objects.get(**params)
        except self.serializer_class.Meta.model.DoesNotExist:
            raise NotFound
