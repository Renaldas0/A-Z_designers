# Generated by Django 3.2 on 2023-01-12 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221229_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]