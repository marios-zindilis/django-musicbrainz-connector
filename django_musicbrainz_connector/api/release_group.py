from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import ReleaseGroup


class ReleaseGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseGroup
        fields = "__all__"


class ReleaseGroupViewSet(viewsets.ModelViewSet):
    queryset = ReleaseGroup.objects.all()
    serializer_class = ReleaseGroupSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
