# Generated by Django 4.2 on 2023-11-17 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0047_alter_authuser_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='roles',
        ),
        migrations.AlterModelTable(
            name='authuser',
            table=None,
        ),
    ]