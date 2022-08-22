# Generated by Django 4.1 on 2022-08-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_remove_product_list_price_productbycompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productbycompany',
            name='product',
        ),
        migrations.AddField(
            model_name='productbycompany',
            name='product',
            field=models.ManyToManyField(to='core.product'),
        ),
    ]
