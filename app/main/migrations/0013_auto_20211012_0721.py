# Generated by Django 3.2.4 on 2021-10-12 07:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211012_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 7, 21, 48, 820865, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 7, 21, 48, 820122, tzinfo=utc)),
        ),
    ]
