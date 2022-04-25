# Generated by Django 3.2 on 2022-04-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_boat_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boat',
            old_name='manufacturer',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='fuel',
            new_name='power_source',
        ),
        migrations.RenameField(
            model_name='boat',
            old_name='condition',
            new_name='state_of_assembly',
        ),
        migrations.RemoveField(
            model_name='boat',
            name='location',
        ),
        migrations.RemoveField(
            model_name='boat',
            name='year_built',
        ),
        migrations.AddField(
            model_name='boat',
            name='age_range',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boat',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='boat',
            name='name',
            field=models.CharField(default='test', max_length=254),
        ),
        migrations.AddField(
            model_name='boat',
            name='speed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
