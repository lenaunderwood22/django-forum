# Generated by Django 3.2.7 on 2021-10-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='static/img/avatar.png', null=True, upload_to='avatar', verbose_name='Avatar'),
        ),
    ]
