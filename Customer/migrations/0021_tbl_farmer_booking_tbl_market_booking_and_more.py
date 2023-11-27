# Generated by Django 4.2.3 on 2023-07-10 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0011_alter_tbl_cus_reg_cus_contact_and_more'),
        ('Farmer', '0013_initial'),
        ('Market', '0015_initial'),
        ('Customer', '0020_remove_tbl_farmer_cart_bookingid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_farmer_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(default='0', max_length=1)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('fpayment_date', models.DateField(null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_cus_reg')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_market_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(default='0', max_length=1)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('mpayment_date', models.DateField(null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_cus_reg')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_market_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mquantity', models.FloatField(default='0', max_length=1)),
                ('mcart_status', models.IntegerField(default='0')),
                ('bookingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.tbl_market_booking')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.tbl_market_product')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_farmer_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fquantity', models.FloatField(default='0', max_length=1)),
                ('fcart_status', models.IntegerField(default='0')),
                ('bookingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.tbl_farmer_booking')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer.tbl_farmer_product')),
            ],
        ),
    ]
