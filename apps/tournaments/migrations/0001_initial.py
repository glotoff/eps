# Generated by Django 4.1.8 on 2023-04-20 06:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clubs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "clubOrganizer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="clubs.club",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]