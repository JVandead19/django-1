# Generated by Django 4.2 on 2023-10-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0010_alter_estudiante_promedio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='Fecha_de_nac',
            new_name='fecha_de_nac',
        ),
    ]
