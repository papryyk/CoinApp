# Generated by Django 4.2 on 2023-07-11 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0015_calldata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranges',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranges', to='hub.calldata'),
        ),
    ]
