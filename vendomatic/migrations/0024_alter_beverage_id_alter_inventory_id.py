# Generated by Django 4.1 on 2022-09-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendomatic', '0023_alter_beverage_inventory_id_alter_beverage_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
