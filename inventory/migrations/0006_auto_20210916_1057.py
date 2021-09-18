# Generated by Django 3.2.6 on 2021-09-16 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_itemmodel_productmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='Itemid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='Pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.productmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='Pid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]