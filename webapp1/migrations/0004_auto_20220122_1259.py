# Generated by Django 2.1.5 on 2022-01-22 06:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0003_auto_20220122_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='esami_sostenuti_e_relativi_esiti',
            name='Student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp1.Verifica_Risultati_Candidato'),
        ),
        migrations.AlterField(
            model_name='verifica_risultati_candidato',
            name='DATA_DI_NASCITA',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 22, 12, 59, 35, 445983)),
        ),
    ]
