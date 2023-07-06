# Generated by Django 4.2 on 2023-06-24 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0010_delete_ranges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calldata',
            name='current_price',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
        migrations.CreateModel(
            name='Ranges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_range', models.DecimalField(decimal_places=10, default=1, max_digits=20, null=True)),
                ('max_range', models.DecimalField(decimal_places=10, default=1, max_digits=20, null=True)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranges', to='hub.calldata')),
            ],
        ),
    ]