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
