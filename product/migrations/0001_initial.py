# Generated by Django 4.1.5 on 2023-02-02 17:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("name", models.CharField(max_length=150, verbose_name="Наименование")),
                (
                    "modification",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Версия",
                    ),
                ),
                (
                    "release_date",
                    models.DateField(
                        blank=True,
                        default=datetime.date,
                        null=True,
                        verbose_name="Дата выпуска",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                ("photo", models.ImageField(blank=True, null=True, upload_to="image/")),
                ("price", models.FloatField(verbose_name="Цена")),
                (
                    "date_org",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
            ],
            options={"verbose_name": "Продукт", "verbose_name_plural": "Продукты",},
        ),
        migrations.CreateModel(
            name="Version",
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
                ("title", models.CharField(max_length=100, verbose_name="Версия")),
                (
                    "release_date",
                    models.DateField(
                        blank=True,
                        default=datetime.date,
                        null=True,
                        verbose_name="Дата выпуска",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={"verbose_name": "Версия", "verbose_name_plural": "Версии",},
        ),
    ]
