# Generated by Django 3.2.4 on 2021-10-12 09:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211012_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 9, 14, 4, 541824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 9, 14, 4, 541086, tzinfo=utc)),
        ),
    ]
