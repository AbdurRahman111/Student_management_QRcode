# Generated by Django 2.1.5 on 2022-01-22 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0004_auto_20220122_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifica_risultati_candidato',
            name='show_MATRICOLA',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='esami_sostenuti_e_relativi_esiti',
            name='Data',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 22, 13, 33, 14, 341052)),
        ),
        migrations.AlterField(
            model_name='verifica_risultati_candidato',
            name='DATA_DI_NASCITA',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 22, 13, 33, 14, 340484)),
        ),
    ]