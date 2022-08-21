# Generated by Django 4.1 on 2022-08-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('address_line_1', models.CharField(max_length=32)),
                ('address_line_2', models.CharField(max_length=32)),
            ],
        ),
    ]