# Generated by Django 5.0.3 on 2024-10-06 21:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('lien', models.URLField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
            ],
        ),
    ]
