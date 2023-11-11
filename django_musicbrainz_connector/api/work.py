from rest_framework import pagination, serializers, viewsets

from django_musicbrainz_connector.models import Work


class WorkPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page-size"
    max_page_size = 100
    page_query_param = "page"


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    http_method_names = ["get"]
    pagination_class = WorkPagination
