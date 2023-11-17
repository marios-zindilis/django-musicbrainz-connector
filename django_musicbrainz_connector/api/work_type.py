import uuid

from django.http import Http404
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django_musicbrainz_connector.models import WorkType


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = "__all__"


class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    http_method_names = ["get"]

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by either the MusicBrainz ID (an
        integer) or the GID (a UUID).
        """
        pk = self.kwargs["pk"]
        try:
            uuid.UUID(pk)
        except (AttributeError, ValueError):
            params = {"pk": pk}
        else:
            params = {"gid": pk}
        return self.serializer_class.Meta.model.objects.get(**params)
