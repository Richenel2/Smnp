# Generated by Django 3.2.5 on 2021-10-05 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smnp_search', '0003_alter_equipement_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='use',
            old_name='quantite',
            new_name='inOctect',
        ),
        migrations.RemoveField(
            model_name='use',
            name='idEquipement',
        ),
        migrations.AddField(
            model_name='use',
            name='outOctect',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oids', models.IntegerField()),
                ('description', models.CharField(max_length=40)),
                ('idEquipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smnp_search.equipement')),
            ],
            options={
                'verbose_name': 'Interface',
            },
        ),
        migrations.AddField(
            model_name='use',
            name='idInterface',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smnp_search.interface'),
            preserve_default=False,
        ),
    ]
