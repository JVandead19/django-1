# Generated by Django 4.2 on 2023-11-17 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0052_alter_authuser_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False},
        ),
    ]
