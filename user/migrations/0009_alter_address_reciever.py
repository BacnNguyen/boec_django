# Generated by Django 3.2b1 on 2021-06-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_address_reciever'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='reciever',
            field=models.CharField(default='Name of reciever', max_length=255),
        ),
    ]
