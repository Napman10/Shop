# Generated by Django 3.0.3 on 2020-05-21 21:02

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_product_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
