from rest_framework import pagination


class DjangoMusicBrainzConnectorPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page-size"
    max_page_size = 100
    page_query_param = "page"
