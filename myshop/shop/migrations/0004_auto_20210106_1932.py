# Generated by Django 3.1.5 on 2021-01-06 19:32

import django.core.validators
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210106_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='products/21/01/06/image.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[250, 250], upload_to='products/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
