# Generated by Django 4.1 on 2022-08-22 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_remove_product_maker_alter_auction_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='list_price',
        ),
        migrations.CreateModel(
            name='ProductByCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('maker', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.company')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
            ],
        ),
    ]
