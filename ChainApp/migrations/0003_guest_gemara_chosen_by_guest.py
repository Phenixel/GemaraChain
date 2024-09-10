# Generated by Django 5.0.3 on 2024-09-10 13:49
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChainApp', '0002_session_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
            },
        ),
        migrations.AddField(
            model_name='gemara',
            name='chosen_by_guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ChainApp.guest'),
        ),
    ]