# Generated by Django 2.2 on 2019-04-26 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('departamentos', '0002_departamento_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='empresa',
        ),
        migrations.AddField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
            preserve_default=False,
        ),
    ]