# Generated by Django 4.1 on 2022-08-21 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.contact'),
        ),
    ]
