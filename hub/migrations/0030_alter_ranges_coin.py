# Generated by Django 5.0 on 2024-01-03 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0029_alter_ranges_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranges',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranges', to='hub.coin'),
        ),
    ]
