# Generated by Django 3.2.5 on 2021-10-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smnp_search', '0004_auto_20211005_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='idEquipement',
            field=models.IntegerField(),
        ),
    ]
