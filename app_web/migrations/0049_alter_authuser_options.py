# Generated by Django 4.2 on 2023-11-17 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0048_remove_authuser_roles_alter_authuser_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False},
        ),
    ]
