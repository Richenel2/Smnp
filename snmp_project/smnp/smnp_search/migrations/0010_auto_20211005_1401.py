# Generated by Django 3.2.5 on 2021-10-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smnp_search', '0009_auto_20211005_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='ip',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='interface',
            name='oids',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='use',
            name='inOctect',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='use',
            name='outOctect',
            field=models.IntegerField(),
        ),
    ]