# Generated by Django 4.1.2 on 2023-05-30 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ShippingAddress',
            new_name='shipping_address',
        ),
    ]