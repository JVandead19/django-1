# Generated by Django 4.2 on 2023-10-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0004_remove_primerlapso_observacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='municipio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='direccion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
