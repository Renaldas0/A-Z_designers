# Generated by Django 3.2 on 2023-01-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shoe_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]