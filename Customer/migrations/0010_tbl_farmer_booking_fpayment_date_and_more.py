# Generated by Django 4.2 on 2023-06-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0009_alter_tbl_farmer_cart_fquantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_farmer_booking',
            name='fpayment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tbl_farmer_cart',
            name='fcart_status',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='tbl_market_booking',
            name='mpayment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tbl_market_cart',
            name='mcart_status',
            field=models.IntegerField(default='0'),
        ),
    ]
