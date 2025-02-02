# Generated by Django 3.2.7 on 2021-10-05 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='status',
            field=models.CharField(choices=[('N', 'Newbie'), ('P', 'Pro')], default='Newbie', max_length=200),
        ),
        migrations.AddField(
            model_name='author',
            name='user_name',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 9, 29, 44, 622995, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 9, 29, 44, 621968, tzinfo=utc)),
        ),
    ]
