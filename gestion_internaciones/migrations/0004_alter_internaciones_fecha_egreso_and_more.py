# Generated by Django 4.2.7 on 2023-11-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_internaciones', '0003_alter_pacientes_estado_pac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internaciones',
            name='fecha_egreso',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internaciones',
            name='hora_egreso',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
