# Generated by Django 4.2.7 on 2023-11-27 19:12

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_internaciones', '0004_alter_internaciones_fecha_egreso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drogueria',
            name='descripcion_drog',
            field=models.TextField(default=builtins.id),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drogueria',
            name='tipo_drog',
            field=models.CharField(default=builtins.id, max_length=20),
            preserve_default=False,
        ),
    ]