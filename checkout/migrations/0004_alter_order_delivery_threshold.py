# Generated by Django 3.2 on 2022-04-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_delivery_threshold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_threshold',
            field=models.DecimalField(decimal_places=2, default=100000, max_digits=6),
        ),
    ]
