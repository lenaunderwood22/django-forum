# Generated by Django 3.2.4 on 2021-10-12 07:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211012_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 7, 6, 37, 714208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 7, 6, 37, 713453, tzinfo=utc)),
        ),
    ]
