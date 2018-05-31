# Generated by Django 2.0.5 on 2018-05-31 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creating_date', models.DateTimeField(auto_now_add=True)),
                ('fav_product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='fav_product_product', to='product.Product')),
                ('fav_substitute', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='fav_substitute_product', to='product.Product')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'fav_product', 'fav_substitute')},
        ),
    ]
