# Generated by Django 4.2 on 2023-06-24 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_remove_calldata_data_calldata_current_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calldata',
            name='name',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='calldata',
            name='symbol',
            field=models.TextField(null=True, unique=True),
        ),
    ]