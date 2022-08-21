# Generated by Django 4.1 on 2022-08-21 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_product_maker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='products',
        ),
        migrations.AddField(
            model_name='company',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]