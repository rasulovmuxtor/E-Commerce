# Generated by Django 3.1.5 on 2021-01-21 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20210121_1038'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Order',
        ),
    ]
