# Generated by Django 5.1.1 on 2024-10-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_currency_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='is_active',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('hold', 'Hold'), ('soft_deleted', 'Soft Deleted')], default='inactive', max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalcurrency',
            name='is_active',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('hold', 'Hold'), ('soft_deleted', 'Soft Deleted')], default='inactive', max_length=20),
        ),
    ]
