# Generated by Django 5.0.1 on 2024-02-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post_counted_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(to="blog.category"),
        ),
    ]
