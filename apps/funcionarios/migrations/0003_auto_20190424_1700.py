# Generated by Django 2.1.7 on 2019-04-24 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190423_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='user',
            new_name='user_id',
        ),
    ]
