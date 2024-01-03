"""
CREATE TABLE release_group_primary_type ( -- replicate
    id                  SERIAL,
    name                VARCHAR(255) NOT NULL,
    parent              INTEGER, -- references release_group_primary_type.id
    child_order         INTEGER NOT NULL DEFAULT 0,
    description         TEXT,
    gid                 uuid NOT NULL
);
"""

from django.db import models


class ReleaseGroupPrimaryType(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    name = models.CharField(max_length=255, db_column="name")
    parent = models.ForeignKey("self", db_column="parent", null=True, on_delete=models.PROTECT)
    child_order = models.IntegerField("Child Order", db_column="child_order")
    description = models.TextField(db_column="description")
    gid = models.UUIDField("GID", db_column="gid")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "release_group_primary_type"
        verbose_name_plural = "Release Group Primary Types"
        ordering = ["name"]
