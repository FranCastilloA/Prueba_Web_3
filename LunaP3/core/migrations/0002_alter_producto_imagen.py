# Generated by Django 4.0.5 on 2022-06-09 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Url Imagen Producto'),
        ),
    ]
