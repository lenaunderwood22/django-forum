# Generated by Django 3.2.7 on 2021-10-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='anonymous', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
