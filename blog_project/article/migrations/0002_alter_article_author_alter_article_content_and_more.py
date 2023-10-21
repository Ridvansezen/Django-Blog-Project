# Generated by Django 4.2.4 on 2023-08-31 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Yazar",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(max_length=500, verbose_name="Açıklama"),
        ),
        migrations.AlterField(
            model_name="article",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Oluşturulma tarihi"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Başlık"),
        ),
    ]
