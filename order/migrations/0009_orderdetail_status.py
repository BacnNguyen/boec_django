# Generated by Django 3.1.7 on 2021-06-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_orderdetail_is_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='status',
            field=models.CharField(choices=[('C', 'Chò xử lí'), ('Đ', 'Đã xác nhận'), ('ĐG', 'Đang gói hàng'), ('V', 'Đang vận chuyển'), ('GH', 'Đang giao hàng'), ('HT', 'Đã hoàn thành')], default=('C', 'Chò xử lí'), max_length=2),
        ),
    ]