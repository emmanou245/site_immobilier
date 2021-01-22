# Generated by Django 3.1.3 on 2021-01-20 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieMaison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_chambre', models.IntegerField(null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('description', models.TextField(null=True)),
                ('prix', models.FloatField(null=True)),
                ('latitude', models.IntegerField(null=True)),
                ('longitude', models.IntegerField(null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('categorie', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backoffice.categoriemaison')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('en instance', 'en instance'), ('non occuper', 'non occuper'), ('occupé', 'occupé')], max_length=200, null=True)),
                ('telephone', models.IntegerField(null=True)),
                ('message', models.TextField(null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('maison', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backoffice.maison')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]