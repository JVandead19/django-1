# Generated by Django 4.2 on 2023-10-12 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0006_authuser_estudiante_userr'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
