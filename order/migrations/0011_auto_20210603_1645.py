# Generated by Django 3.1.7 on 2021-06-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20210603_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Chờ xác nhận'), ('2', 'Chờ lấy hàng'), ('3', 'Đang vận chuyển'), ('4', 'Đang giao hàng'), ('5', 'Đã hoàn thành'), ('6', 'Đã hủy')], default=('1', 'Chờ xác nhận'), max_length=2),
        ),
    ]
