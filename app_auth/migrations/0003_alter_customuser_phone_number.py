# Generated by Django 5.1 on 2024-08-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0002_customuser_email_customuser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(help_text='Enter a valid Bangladeshi phone number.', max_length=15),
        ),
    ]
