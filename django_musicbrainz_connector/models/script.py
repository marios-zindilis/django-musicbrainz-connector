"""
CREATE TABLE script ( -- replicate
    id                  SERIAL,
    iso_code            CHAR(4) NOT NULL, -- ISO 15924
    iso_number          CHAR(3) NOT NULL, -- ISO 15924
    name                VARCHAR(100) NOT NULL,
    frequency           SMALLINT NOT NULL DEFAULT 0
);
"""

from django.db import models


class Script(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    iso_code = models.CharField("ISO Code", max_length=4, db_column="iso_code")
    iso_number = models.CharField("ISO Number", max_length=3, db_column="iso_number")
    name = models.CharField("Name", max_length=100, db_column="name")
    frequency = models.SmallIntegerField("Frequency", default=0, db_column="frequency")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "script"
        verbose_name_plural = "Scripts"
        ordering = ["name"]
