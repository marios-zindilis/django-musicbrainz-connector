from django.urls import include, path
from rest_framework import routers

from django_musicbrainz_connector.api.work import WorkViewSet
from django_musicbrainz_connector.api.work_type import WorkTypeViewSet

router = routers.DefaultRouter()
router.register(r"works", WorkViewSet)
router.register(r"work-types", WorkTypeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
