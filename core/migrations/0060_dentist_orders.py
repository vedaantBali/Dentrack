# Generated by Django 4.1 on 2022-08-28 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='orders',
            field=models.ManyToManyField(related_name='dentist_order', to='core.order'),
        ),
    ]
