# Generated by Django 5.1.5 on 2025-03-10 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_alter_post_author_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.CharField(max_length=100),
        ),
    ]
