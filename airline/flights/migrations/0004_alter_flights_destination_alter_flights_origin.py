# Generated by Django 5.0 on 2024-05-29 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_alter_flights_destination_alter_flights_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.aiport'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='flights.aiport'),
        ),
    ]
