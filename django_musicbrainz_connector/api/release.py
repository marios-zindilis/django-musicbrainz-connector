from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.api.language import LanguageSerializer
from django_musicbrainz_connector.api.medium import MediumSerializer
from django_musicbrainz_connector.api.script import ScriptSerializer
from django_musicbrainz_connector.models import Release
from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


class ReleaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["language"] = LanguageSerializer(instance.language).data
        representation["media"] = [MediumSerializer(medium).data for medium in instance.media.all()]
        representation["script"] = ScriptSerializer(instance.script).data
        return representation

    class Meta:
        model = Release
        fields = "__all__"


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by either the MusicBrainz ID (an
        integer) or the MusicBrainz GID (a UUID). Call with something like:

            GET /api/releases/a026f47e-5ce7-4b6f-8469-cdf8c4bccb4b

        Or:

            GET /api/releases/2681644
        """
        pk = self.kwargs["pk"]
        pk_type = get_musicbrainz_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return Release.objects.get(**params)
        except Release.DoesNotExist:
            raise NotFound
