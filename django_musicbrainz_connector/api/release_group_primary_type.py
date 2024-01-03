from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import ReleaseGroupPrimaryType


class ReleaseGroupPrimaryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseGroupPrimaryType
        fields = "__all__"


class ReleaseGroupPrimaryTypeViewSet(viewsets.ModelViewSet):
    queryset = ReleaseGroupPrimaryType.objects.all()
    serializer_class = ReleaseGroupPrimaryTypeSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
