# Generated by Django 4.1 on 2022-08-21 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentist',
            name='inventory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.item'),
        ),
    ]
