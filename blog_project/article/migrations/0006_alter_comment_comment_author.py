# Generated by Django 4.2.4 on 2023-09-10 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0005_alter_article_description_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="İsim",
            ),
        ),
    ]
