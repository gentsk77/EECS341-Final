# Generated by Django 2.0.13 on 2019-04-28 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='length',
        ),
        migrations.AddField(
            model_name='membership',
            name='expired_date',
            field=models.DateField(default=datetime.date(2019, 5, 28)),
        ),
    ]
