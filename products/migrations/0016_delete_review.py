# Generated by Django 3.2 on 2023-02-22 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_review_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
