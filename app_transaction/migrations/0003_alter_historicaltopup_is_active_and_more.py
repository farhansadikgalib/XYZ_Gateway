# Generated by Django 5.1.1 on 2024-10-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transaction', '0002_topup_historicaltopup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltopup',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='historicaltransaction',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
