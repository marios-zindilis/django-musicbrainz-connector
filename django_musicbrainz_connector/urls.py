from django.urls import include, path
from rest_framework import routers

from django_musicbrainz_connector.api.artist_credit import ArtistCreditViewSet
from django_musicbrainz_connector.api.link import LinkViewSet
from django_musicbrainz_connector.api.link_type import LinkTypeViewSet
from django_musicbrainz_connector.api.recording import RecordingViewSet
from django_musicbrainz_connector.api.recording_work_link import RecordingWorkLinkViewSet
from django_musicbrainz_connector.api.script import ScriptViewSet
from django_musicbrainz_connector.api.work import WorkViewSet
from django_musicbrainz_connector.api.work_type import WorkTypeViewSet

router = routers.DefaultRouter()
router.register(r"artist-credits", ArtistCreditViewSet)
router.register(r"links", LinkViewSet)
router.register(r"link-types", LinkTypeViewSet)
router.register(r"recordings", RecordingViewSet)
router.register(r"recording-work-links", RecordingWorkLinkViewSet)
router.register(r"scripts", ScriptViewSet)
router.register(r"works", WorkViewSet)
router.register(r"work-types", WorkTypeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
