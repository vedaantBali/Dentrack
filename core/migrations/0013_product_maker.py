# Generated by Django 4.1 on 2022-08-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_company_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='maker',
            field=models.ManyToManyField(blank=True, null=True, to='core.company'),
        ),
    ]