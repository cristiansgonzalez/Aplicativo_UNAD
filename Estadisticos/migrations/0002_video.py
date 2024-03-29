# Generated by Django 4.1.1 on 2022-11-16 21:48

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ("Estadisticos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("added", models.DateTimeField(auto_now_add=True)),
                ("url", embed_video.fields.EmbedVideoField()),
            ],
            options={
                "verbose_name": "Video",
                "verbose_name_plural": "Videos",
                "db_table": "video",
                "ordering": ["-added"],
            },
        ),
    ]
