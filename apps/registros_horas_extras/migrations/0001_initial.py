# Generated by Django 2.1.7 on 2019-04-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroHoraExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'RegistroHoraExtra',
                'verbose_name_plural': 'Registros Horas Extras',
            },
        ),
    ]
