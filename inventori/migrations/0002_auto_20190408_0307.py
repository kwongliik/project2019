# Generated by Django 2.1.7 on 2019-04-08 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventori', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventori',
            name='inventori',
            field=models.CharField(max_length=50),
        ),
    ]