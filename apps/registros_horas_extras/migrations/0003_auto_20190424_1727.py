# Generated by Django 2.2 on 2019-04-24 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros_horas_extras', '0002_auto_20190423_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrohoraextra',
            old_name='motivo',
            new_name='motivo_hora_extra',
        ),
    ]