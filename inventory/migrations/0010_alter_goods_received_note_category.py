# Generated by Django 3.2.6 on 2021-09-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20210917_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods_received_note',
            name='category',
            field=models.CharField(default='category', max_length=400),
        ),
    ]