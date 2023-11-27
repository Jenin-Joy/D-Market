# Generated by Django 4.2.3 on 2023-07-08 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0020_tbl_catageory_tbl_complainttype_tbl_farmtype_and_more'),
        ('Guest', '0009_remove_tbl_cus_reg_cus_locplace_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cus_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=50)),
                ('cus_contact', models.CharField(max_length=10)),
                ('cus_email', models.CharField(max_length=50)),
                ('cus_address', models.CharField(max_length=100)),
                ('cus_photo', models.FileField(upload_to='CustomerPhoto/')),
                ('cus_pass', models.CharField(max_length=50)),
                ('cus_doj', models.DateField(auto_now_add=True)),
                ('cus_locplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_local_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_farmer_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('far_name', models.CharField(max_length=50)),
                ('far_email', models.CharField(max_length=50)),
                ('far_contact', models.CharField(max_length=10)),
                ('far_address', models.CharField(max_length=100)),
                ('far_photo', models.FileField(upload_to='FarmerPhoto/')),
                ('far_proof', models.FileField(upload_to='FarmerproofPhoto/')),
                ('far_pass', models.CharField(max_length=50)),
                ('far_doj', models.DateField(auto_now_add=True)),
                ('far_status', models.CharField(default='0', max_length=1)),
                ('farmer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_farmtype')),
                ('locplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_local_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_market_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mar_name', models.CharField(max_length=50)),
                ('mar_email', models.CharField(max_length=50)),
                ('mar_contact', models.CharField(max_length=10)),
                ('mar_address', models.CharField(max_length=100)),
                ('marphoto', models.FileField(upload_to='MarketPhoto/')),
                ('marproof', models.FileField(upload_to='Marketproof/')),
                ('marpassword', models.CharField(max_length=50)),
                ('mar_doj', models.DateField(auto_now_add=True)),
                ('mar_status', models.CharField(default='0', max_length=1)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_con', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_cus_reg')),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_farmer_reg')),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_market_reg')),
                ('subadmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_subadmin')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_con', models.CharField(max_length=500)),
                ('sdate', models.DateField(auto_now_add=True)),
                ('rdate', models.DateField(null=True)),
                ('replay', models.CharField(max_length=500)),
                ('status', models.CharField(default='0', max_length=1)),
                ('com_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_complainttype')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_cus_reg')),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_farmer_reg')),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_market_reg')),
                ('subadmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.tbl_subadmin')),
            ],
        ),
    ]