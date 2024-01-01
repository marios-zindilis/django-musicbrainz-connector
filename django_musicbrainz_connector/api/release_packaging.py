from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import ReleasePackaging


class ReleasePackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleasePackaging
        fields = "__all__"


class ReleasePackagingViewSet(viewsets.ModelViewSet):
    queryset = ReleasePackaging.objects.all()
    serializer_class = ReleasePackagingSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
