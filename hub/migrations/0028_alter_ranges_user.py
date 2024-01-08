# Generated by Django 5.0 on 2024-01-03 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0027_ranges_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranges',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ranges', to='hub.user'),
        ),
    ]