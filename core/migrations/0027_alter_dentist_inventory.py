# Generated by Django 4.1 on 2022-08-21 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_inventory_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.inventory'),
        ),
    ]
