# Generated by Django 4.2 on 2023-11-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0024_coin_cg_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
