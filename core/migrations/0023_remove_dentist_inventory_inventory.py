# Generated by Django 4.1 on 2022-08-21 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_dentist_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dentist',
            name='inventory',
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.item')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.dentist')),
            ],
        ),
    ]
