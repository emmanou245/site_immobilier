# Generated by Django 3.1.3 on 2021-01-25 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backoffice', '0006_auto_20210124_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('en instance', 'en instance'), ('non occuper', 'non occuper'), ('occupé', 'occupé')], max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='Requette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=256, null=True)),
                ('quartier', models.CharField(max_length=256, null=True)),
                ('message', models.TextField(null=True)),
                ('telephone', models.IntegerField(null=True)),
                ('prix', models.IntegerField(null=True)),
                ('categorie', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backoffice.categoriemaison')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
