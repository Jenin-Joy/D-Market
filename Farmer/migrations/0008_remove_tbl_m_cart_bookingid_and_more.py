# Generated by Django 4.2.3 on 2023-07-06 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0007_tbl_m_booking_payment_date_tbl_m_cart_cart_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_m_cart',
            name='bookingid',
        ),
        migrations.RemoveField(
            model_name='tbl_m_cart',
            name='productid',
        ),
        migrations.DeleteModel(
            name='tbl_m_booking',
        ),
        migrations.DeleteModel(
            name='tbl_m_cart',
        ),
    ]
