# Generated by Django 4.2 on 2023-05-26 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_tbl_market_reg_mar_status'),
        ('Customer', '0002_tbl_farmer_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tbl_booking',
            new_name='tbl_farmer_booking',
        ),
    ]