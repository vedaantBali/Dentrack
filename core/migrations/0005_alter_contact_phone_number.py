# Generated by Django 4.1 on 2022-08-21 05:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contact_pin_code_contact_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
