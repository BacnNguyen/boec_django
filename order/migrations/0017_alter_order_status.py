# Generated by Django 3.2b1 on 2021-06-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Chờ xác nhận'), (2, 'Đang xử lí'), (3, 'Đang giao hàng'), (4, 'Đã hoàn thành'), (5, 'Đã hủy')], default=1),
        ),
    ]
