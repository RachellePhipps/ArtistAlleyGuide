# Generated by Django 5.1.6 on 2025-03-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conventions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('con_date', models.DateField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('website', models.CharField(max_length=64)),
                ('num_attend', models.IntegerField()),
                ('apply_date', models.DateField()),
                ('table_cost', models.IntegerField()),
                ('travel_cost', models.IntegerField()),
                ('num_artists', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
