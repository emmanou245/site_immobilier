# Generated by Django 3.1.3 on 2021-01-21 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maison',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='maison',
            name='longitude',
        ),
    ]