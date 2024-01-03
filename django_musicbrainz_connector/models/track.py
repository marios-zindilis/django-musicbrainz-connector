"""
CREATE TABLE track ( -- replicate (verbose)
    id                  SERIAL,
    gid                 UUID NOT NULL,
    recording           INTEGER NOT NULL, -- references recording.id
    medium              INTEGER NOT NULL, -- references medium.id
    position            INTEGER NOT NULL,
    number              TEXT NOT NULL,
    name                VARCHAR NOT NULL,
    artist_credit       INTEGER NOT NULL, -- references artist_credit.id
    length              INTEGER CHECK (length IS NULL OR length > 0),
    edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_data_track       BOOLEAN NOT NULL DEFAULT FALSE
);
"""

from django.db import models


class Track(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField("GID", db_column="gid")
    recording = models.ForeignKey(
        "Recording",
        verbose_name="Recording",
        related_name="tracks",
        on_delete=models.PROTECT,
        db_column="recording",
    )
    medium = models.ForeignKey(
        "Medium",
        verbose_name="Medium",
        related_name="tracks",
        on_delete=models.PROTECT,
        db_column="medium",
    )
    position = models.IntegerField("Position", db_column="position")
    number = models.TextField("Number", db_column="number")
    name = models.CharField(max_length=2048, db_column="name")
    artist_credit = models.ForeignKey(
        "ArtistCredit",
        verbose_name="Artist Credit",
        related_name="tracks",
        on_delete=models.PROTECT,
        db_column="artist_credit",
    )
    length = models.PositiveIntegerField("Length", null=True, blank=True, db_column="length")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")
    is_data_track = models.BooleanField("Is Data Track?", default=False, db_column="is_data_track")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "track"
        verbose_name_plural = "Tracks"
        ordering = ["position"]
