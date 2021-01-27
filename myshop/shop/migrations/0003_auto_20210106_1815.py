# Generated by Django 3.1.5 on 2021-01-06 18:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210106_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='shop.manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
