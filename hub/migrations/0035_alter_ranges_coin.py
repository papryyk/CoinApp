# Generated by Django 5.0 on 2024-01-08 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0034_alter_ranges_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranges',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ranges', to='hub.coin'),
        ),
    ]