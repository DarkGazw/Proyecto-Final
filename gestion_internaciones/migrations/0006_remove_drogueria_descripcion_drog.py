# Generated by Django 4.2.7 on 2023-11-27 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_internaciones', '0005_drogueria_descripcion_drog_drogueria_tipo_drog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drogueria',
            name='descripcion_drog',
        ),
    ]
