"""
CREATE TABLE medium ( -- replicate (verbose)
    id                  SERIAL,
    release             INTEGER NOT NULL, -- references release.id
    position            INTEGER NOT NULL,
    format              INTEGER, -- references medium_format.id
    name                VARCHAR NOT NULL DEFAULT '',
    edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    track_count         INTEGER NOT NULL DEFAULT 0
);
"""

from django.db import models


class Medium(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    release = models.ForeignKey(
        "Release",
        verbose_name="Release",
        related_name="media",
        on_delete=models.PROTECT,
        db_column="release",
    )
    position = models.IntegerField("Position", db_column="position")
    format = models.ForeignKey(
        "MediumFormat",
        verbose_name="Format",
        related_name="media",
        on_delete=models.PROTECT,
        db_column="format",
    )
    name = models.CharField(max_length=2048, db_column="name")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")
    track_count = models.IntegerField("Track Count", default=0, db_column="track_count")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "medium"
        verbose_name_plural = "Media"
        ordering = ["position"]
