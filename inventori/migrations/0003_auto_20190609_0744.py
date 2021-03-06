# Generated by Django 2.1.7 on 2019-06-09 07:44

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventori', '0002_auto_20190408_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventori',
            name='harga',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))]),
        ),
        migrations.AlterField(
            model_name='inventori',
            name='kuantiti',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
