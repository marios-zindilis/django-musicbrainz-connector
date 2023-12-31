# Generated by Django 4.2.7 on 2023-11-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WorkType",
            fields=[
                ("id", models.IntegerField(db_column="id", primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_column="name", max_length=255)),
                ("child_order", models.IntegerField(db_column="child_order", verbose_name="Child Order")),
                ("description", models.TextField(db_column="description")),
            ],
            options={
                "verbose_name_plural": "Work Types",
                "db_table": "work_type",
                "managed": False,
            },
        ),
    ]
