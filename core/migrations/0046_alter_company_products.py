# Generated by Django 4.1 on 2022-08-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_alter_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='products',
            field=models.ManyToManyField(blank=True, to='core.productbycompany'),
        ),
    ]
