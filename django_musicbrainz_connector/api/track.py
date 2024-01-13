from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.api.recording import RecordingSerializer
from django_musicbrainz_connector.models import Track


class TrackSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["recording"] = RecordingSerializer(instance.recording).data
        return representation

    class Meta:
        model = Track
        fields = "__all__"


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_queryset(self):
        """
        Overriding the default `get_queryset` method of `ModelViewSet` to allow listing Track instances by the medium ID
        (an integer), essentially getting all tracks for a medium. Call with:

            GET /api/tracks/?medium-id=1234
        """
        queryset = Track.objects.all()
        medium_id = self.request.query_params.get("medium-id")
        if medium_id is not None:
            queryset = queryset.filter(medium_id=medium_id)
        return queryset
