# Generated by Django 4.0.5 on 2022-06-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Url Imagen Producto'),
        ),
    ]
