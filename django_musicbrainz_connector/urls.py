from django.urls import include, path
from rest_framework import routers

from django_musicbrainz_connector.api.artist_credit import ArtistCreditViewSet
from django_musicbrainz_connector.api.work import WorkViewSet
from django_musicbrainz_connector.api.work_type import WorkTypeViewSet

router = routers.DefaultRouter()
router.register(r"artist-credits", ArtistCreditViewSet)
router.register(r"works", WorkViewSet)
router.register(r"work-types", WorkTypeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
