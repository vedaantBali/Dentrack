# Generated by Django 4.1 on 2022-08-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='orders',
            field=models.ManyToManyField(related_name='company_order', to='core.order'),
        ),
    ]
