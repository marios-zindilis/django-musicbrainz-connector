from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import RecordingWorkLink


class RecordingWorkLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordingWorkLink
        fields = "__all__"


class RecordingWorkLinkViewSet(viewsets.ModelViewSet):
    queryset = RecordingWorkLink.objects.all()
    serializer_class = RecordingWorkLinkSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
