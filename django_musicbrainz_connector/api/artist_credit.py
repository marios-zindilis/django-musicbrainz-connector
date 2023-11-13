from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import ArtistCredit


class ArtistCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistCredit
        fields = "__all__"


class ArtistCreditViewSet(viewsets.ModelViewSet):
    queryset = ArtistCredit.objects.all()
    serializer_class = ArtistCreditSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
