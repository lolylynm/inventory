# Generated by Django 3.2.6 on 2021-09-22 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210921_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_received_note',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 22, 7, 44, 45, 920196)),
        ),
        migrations.AlterField(
            model_name='issue_receipt_voucher',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 22, 7, 44, 45, 920444)),
        ),
        migrations.AlterField(
            model_name='issue_receipt_voucher',
            name='date1',
            field=models.DateField(default=datetime.datetime(2021, 9, 22, 7, 44, 45, 920515)),
        ),
    ]
