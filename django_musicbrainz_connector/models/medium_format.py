"""
CREATE TABLE medium_format ( -- replicate
    id                  SERIAL,
    name                VARCHAR(100) NOT NULL,
    parent              INTEGER, -- references medium_format.id
    child_order         INTEGER NOT NULL DEFAULT 0,
    year                SMALLINT,
    has_discids         BOOLEAN NOT NULL DEFAULT FALSE,
    description         TEXT,
    gid                 uuid NOT NULL
);
"""

from django.db import models


class MediumFormat(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    name = models.CharField("Name", max_length=100, db_column="name")
    parent = models.ForeignKey("self", db_column="parent", null=True, on_delete=models.PROTECT)
    child_order = models.IntegerField("Child Order", db_column="child_order")
    year = models.SmallIntegerField("Year", null=True, blank=True, db_column="year")
    has_discids = models.BooleanField("Has DiscIDs", default=False, db_column="has_discids")
    description = models.TextField("Description", db_column="description")
    gid = models.UUIDField("GID", db_column="gid")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "medium_format"
        verbose_name_plural = "Medium Formats"
        ordering = ["name"]
