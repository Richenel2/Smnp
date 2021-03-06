# Generated by Django 3.2.7 on 2021-09-28 15:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auteur', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=25)),
                ('communityString', models.CharField(max_length=25, verbose_name='Community String')),
                ('pollerEngine', models.CharField(max_length=25)),
                ('idCategorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smnp_search.categorie')),
            ],
            options={
                'verbose_name': 'Equipement',
            },
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.DateTimeField(default=django.utils.timezone.now, verbose_name='heure')),
                ('quantite', models.IntegerField()),
                ('idEquipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smnp_search.equipement')),
            ],
            options={
                'verbose_name': 'Equipement utilisation',
            },
        ),
        migrations.CreateModel(
            name='Down',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.DateTimeField(default=django.utils.timezone.now, verbose_name='heure')),
                ('idEquipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smnp_search.equipement')),
            ],
            options={
                'verbose_name': 'Equipement Down',
            },
        ),
    ]
