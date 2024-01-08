from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import Medium


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium
        fields = "__all__"


class MediumViewSet(viewsets.ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_queryset(self):
        """
        Overriding the default `get_queryset` method of `ModelViewSet` to allow listing Medium instances by the release
        ID (an integer). Call with:

        GET /api/media/?release-id=1234
        """
        queryset = Medium.objects.all()
        release_id = self.request.query_params.get("release-id")
        if release_id is not None:
            queryset = queryset.filter(release_id=release_id)
        return queryset
