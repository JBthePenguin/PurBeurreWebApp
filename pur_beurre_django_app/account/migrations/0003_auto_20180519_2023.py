# Generated by Django 2.0.5 on 2018-05-19 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180519_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersession',
            name='session',
        ),
        migrations.RemoveField(
            model_name='usersession',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserSession',
        ),
    ]
