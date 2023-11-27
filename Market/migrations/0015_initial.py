# Generated by Django 4.2.3 on 2023-07-08 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0010_initial'),
        ('Admin', '0020_tbl_catageory_tbl_complainttype_tbl_farmtype_and_more'),
        ('Market', '0014_remove_tbl_market_product_market_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_market_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdt_name', models.CharField(max_length=50)),
                ('pdt_rate', models.IntegerField()),
                ('pdt_dis', models.CharField(max_length=100)),
                ('pdt_stock', models.FloatField()),
                ('pdt_image', models.FileField(upload_to='MarketProduct/')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_market_reg')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subcat')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_fdate', models.DateField(null=True)),
                ('event_tdate', models.DateField(null=True)),
                ('event_details', models.CharField(max_length=500)),
                ('event_photo', models.FileField(upload_to='MarketEvents/')),
                ('status', models.CharField(default='0', max_length=1)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_market_reg')),
            ],
        ),
    ]
