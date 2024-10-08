# Generated by Django 5.1.1 on 2024-10-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_experiencia"),
    ]

    operations = [
        migrations.CreateModel(
            name="Educacion",
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
                ("titulo", models.CharField(max_length=255)),
                ("institucion", models.CharField(max_length=255)),
                ("anio_inicio", models.IntegerField()),
                ("anio_fin", models.IntegerField()),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
