# Generated by Django 3.2 on 2022-04-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
