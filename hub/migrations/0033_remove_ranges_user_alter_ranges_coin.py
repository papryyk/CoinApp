# Generated by Django 5.0 on 2024-01-03 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0032_alter_ranges_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranges',
            name='user',
        ),
        migrations.AlterField(
            model_name='ranges',
            name='coin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ranges', to='hub.coin'),
        ),
    ]
