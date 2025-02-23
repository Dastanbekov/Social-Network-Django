# Generated by Django 5.1.4 on 2025-02-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug'),
        ),
    ]
