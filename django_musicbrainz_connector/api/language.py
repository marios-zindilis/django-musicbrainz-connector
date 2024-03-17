from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import Language
from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by either ID (the numeric ID from
        MusicBrainz), or by the name of the Language. This assumes that names of languages are unique.

        Either of these calls should work:

            GET /api/languages/159
            GET /api/languages/Greek
        """
        pk = self.kwargs["pk"]
        pk_type = get_musicbrainz_identifier_type(pk)  # either "id" or "gid" or "name"
        params = {pk_type: pk}
        try:
            return Language.objects.get(**params)
        except Language.DoesNotExist:
            raise NotFound
