# Generated by Django 3.1.3 on 2021-01-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0009_auto_20210126_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requette',
            name='prix',
            field=models.FloatField(null=True),
        ),
    ]
