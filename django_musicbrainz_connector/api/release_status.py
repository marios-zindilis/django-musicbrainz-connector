from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import ReleaseStatus


class ReleaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseStatus
        fields = "__all__"


class ReleaseStatusViewSet(viewsets.ModelViewSet):
    queryset = ReleaseStatus.objects.all()
    serializer_class = ReleaseStatusSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
