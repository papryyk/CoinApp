# Generated by Django 4.2 on 2023-06-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_calldata_upload_time_alter_calldata_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calldata',
            name='current_price',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]
