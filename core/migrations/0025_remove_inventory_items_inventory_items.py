# Generated by Django 4.1 on 2022-08-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_dentist_inventory_alter_inventory_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='items',
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.ManyToManyField(null=True, to='core.item'),
        ),
    ]