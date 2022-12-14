# Generated by Django 4.1 on 2022-08-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_contact_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(choices=[('Port Blair', 'Port Blair'), ('Adoni', 'Adoni'), ('Amaravati', 'Amaravati'), ('Anantapur', 'Anantapur'), ('Chandragiri', 'Chandragiri'), ('Chittoor', 'Chittoor'), ('Dowlaiswaram', 'Dowlaiswaram'), ('Eluru', 'Eluru'), ('Guntur', 'Guntur'), ('Kadapa', 'Kadapa'), ('Kakinada', 'Kakinada'), ('Kurnool', 'Kurnool'), ('Machilipatnam', 'Machilipatnam'), ('Nagarjunakoṇḍa', 'Nagarjunakoṇḍa'), ('Rajahmundry', 'Rajahmundry'), ('Srikakulam', 'Srikakulam'), ('Tirupati', 'Tirupati'), ('Vijayawada', 'Vijayawada'), ('Visakhapatnam', 'Visakhapatnam'), ('Vizianagaram', 'Vizianagaram'), ('Yemmiganur', 'Yemmiganur')], max_length=64, null=True),
        ),
    ]
