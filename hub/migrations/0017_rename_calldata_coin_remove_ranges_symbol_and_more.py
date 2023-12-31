# Generated by Django 4.2 on 2023-07-11 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0016_alter_ranges_symbol'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CallData',
            new_name='Coin',
        ),
        migrations.RemoveField(
            model_name='ranges',
            name='symbol',
        ),
        migrations.AddField(
            model_name='ranges',
            name='coin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ranges', to='hub.coin'),
        ),
    ]
