# Generated by Django 4.2 on 2023-11-17 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0044_alter_authuser_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False},
        ),
    ]
