# Generated by Django 4.2.1 on 2023-05-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_country_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='flag',
            field=models.ImageField(null=True, upload_to='flags/', verbose_name='Flag'),
        ),
    ]