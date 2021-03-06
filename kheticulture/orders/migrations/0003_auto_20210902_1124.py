# Generated by Django 3.2.7 on 2021-09-02 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210902_1124'),
        ('orders', '0002_remove_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Received'), (2, 'In Process'), (3, 'Out For Delivery'), (4, 'Delivered')], default=1),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.product'),
        ),
    ]
