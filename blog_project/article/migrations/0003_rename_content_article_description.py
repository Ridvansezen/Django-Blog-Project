# Generated by Django 4.2.4 on 2023-08-31 21:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0002_alter_article_author_alter_article_content_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="content",
            new_name="description",
        ),
    ]
