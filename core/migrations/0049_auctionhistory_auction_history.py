# Generated by Django 4.1 on 2022-08-26 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_alter_dentist_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_price', models.IntegerField()),
                ('index', models.IntegerField()),
                ('bid_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='history',
            field=models.ManyToManyField(to='core.auctionhistory'),
        ),
    ]
