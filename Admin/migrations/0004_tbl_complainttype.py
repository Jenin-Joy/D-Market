# Generated by Django 4.2 on 2023-04-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_delete_tbl_complainttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complainttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_type_name', models.CharField(max_length=50)),
            ],
        ),
    ]
