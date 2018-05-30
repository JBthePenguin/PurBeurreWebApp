# Generated by Django 2.0.5 on 2018-05-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField(null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('substitute_id', models.IntegerField(null=True)),
                ('creating_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
