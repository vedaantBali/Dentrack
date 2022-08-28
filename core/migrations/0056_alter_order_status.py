# Generated by Django 4.1 on 2022-08-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('PLACED', 'Placed'), ('RECEIVED', 'Received'), ('PROCESSED', 'Processed'), ('DISPATCHED', 'Dispatched'), ('IN_TRANSIT', 'In Transit'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], max_length=32),
        ),
    ]
