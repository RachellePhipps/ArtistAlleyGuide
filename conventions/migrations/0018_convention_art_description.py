# Generated by Django 5.1.6 on 2025-04-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conventions', '0017_remove_convention_rating_comment_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='convention',
            name='art_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
