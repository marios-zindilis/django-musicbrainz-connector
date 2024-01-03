from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import MediumFormat


class MediumFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediumFormat
        fields = "__all__"


class MediumFormatViewSet(viewsets.ModelViewSet):
    queryset = MediumFormat.objects.all()
    serializer_class = MediumFormatSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
