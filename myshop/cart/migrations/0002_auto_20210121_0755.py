# Generated by Django 3.1.5 on 2021-01-21 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lastname',
            new_name='last_name',
        ),
    ]