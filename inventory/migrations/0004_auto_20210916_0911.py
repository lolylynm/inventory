# Generated by Django 3.2.6 on 2021-09-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210916_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_received_note',
            name='comments',
            field=models.TextField(default='comment', max_length=400),
        ),
        migrations.AlterField(
            model_name='goods_received_note',
            name='quantity',
            field=models.IntegerField(default='Quantity', max_length=400),
        ),
        migrations.AlterField(
            model_name='issue_receipt_voucher',
            name='quantity',
            field=models.IntegerField(default='Quantity', max_length=400),
        ),
    ]
