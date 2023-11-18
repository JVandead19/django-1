# Generated by Django 4.2 on 2023-11-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0030_alter_authuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='docent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='authuser',
            name='roles',
            field=models.CharField(choices=[('usuario', 'Estudiante'), ('docente', 'Docente')], default='usuario', max_length=7),
        ),
        migrations.AlterModelTable(
            name='authuser',
            table=None,
        ),
    ]