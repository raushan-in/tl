# Generated by Django 4.0.4 on 2022-05-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricethresholdnotifications',
            name='lower_threshold_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pricethresholdnotifications',
            name='upper_threshold_flag',
            field=models.BooleanField(default=False),
        ),
    ]
