# Generated by Django 4.2 on 2023-07-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0014_calldata_market_cap_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='calldata',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
