# Generated by Django 2.0.1 on 2019-05-04 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190503_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='memberlevel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'managed': False},
        ),
    ]