# Generated by Django 3.2 on 2022-04-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220408_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='boat',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
