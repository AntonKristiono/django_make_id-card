# Generated by Django 3.1 on 2021-01-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartu', '0006_datamurid_cetak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamurid',
            name='alamat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
