# Generated by Django 3.2.4 on 2021-06-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210626_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='razon_social',
            field=models.CharField(max_length=50, verbose_name='razon social'),
        ),
    ]