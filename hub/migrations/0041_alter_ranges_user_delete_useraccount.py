# Generated by Django 5.0 on 2024-01-08 21:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0040_ranges_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranges',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ranges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
