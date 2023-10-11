# Generated by Django 4.2.4 on 2023-09-10 20:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0008_alter_article_options_alter_comment_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["comment_date"]},
        ),
        migrations.AlterField(
            model_name="comment",
            name="comment_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Kullanıcı",
            ),
        ),
    ]
