from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import LinkType


class LinkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkType
        fields = "__all__"


class LinkTypeViewSet(viewsets.ModelViewSet):
    queryset = LinkType.objects.all()
    serializer_class = LinkTypeSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
