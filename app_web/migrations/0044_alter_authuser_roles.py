# Generated by Django 4.2 on 2023-11-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0043_remove_authuser_docent_alter_authuser_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='roles',
            field=models.CharField(choices=[('usuario', 'Estudiante'), ('docente', 'Docente')], max_length=7),
        ),
    ]
