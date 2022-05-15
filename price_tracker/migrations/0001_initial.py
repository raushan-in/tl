# Generated by Django 4.0.4 on 2022-05-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_id', models.CharField(max_length=50, unique=True)),
                ('coin_name', models.CharField(max_length=50)),
            ],
        ),
    ]