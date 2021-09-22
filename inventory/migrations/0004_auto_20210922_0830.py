# Generated by Django 3.2.6 on 2021-09-22 08:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210922_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue_receipt_voucher',
            name='id1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.goods_received_note'),
        ),
        migrations.AlterField(
            model_name='goods_received_note',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 22, 8, 30, 58, 121586)),
        ),
        migrations.AlterField(
            model_name='issue_receipt_voucher',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 22, 8, 30, 58, 121845)),
        ),
        migrations.AlterField(
            model_name='issue_receipt_voucher',
            name='date1',
            field=models.DateField(default=datetime.datetime(2021, 9, 22, 8, 30, 58, 121912)),
        ),
        migrations.AlterField(
            model_name='issue_receipt_voucher',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]