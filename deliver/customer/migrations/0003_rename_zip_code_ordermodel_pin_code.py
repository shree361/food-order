# Generated by Django 4.1.2 on 2022-10-25 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_ordermodel_city_ordermodel_email_ordermodel_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='zip_code',
            new_name='pin_code',
        ),
    ]
