# Generated by Django 4.1 on 2022-08-21 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_company_products_company_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='maker',
        ),
    ]
