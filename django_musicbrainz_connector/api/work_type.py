from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import WorkType
from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = "__all__"


class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by any unique identifier for a Work
        Type, either the MusicBrainz ID (an integer), or the GID (a UUID), or the name (a string). Call with something
        like:

            GET /api/work-types/Musical/
        """
        pk = self.kwargs["pk"]
        pk_type = get_musicbrainz_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return WorkType.objects.get(**params)
        except WorkType.DoesNotExist:
            raise NotFound
