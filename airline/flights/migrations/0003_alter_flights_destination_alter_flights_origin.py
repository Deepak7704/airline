# Generated by Django 5.0 on 2024-05-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_aiport_alter_flights_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='destination',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='flights',
            name='origin',
            field=models.CharField(max_length=64),
        ),
    ]
