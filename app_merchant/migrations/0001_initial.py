# Generated by Django 5.1.1 on 2024-09-30 17:40

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMerchant',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('version', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=255, verbose_name='merchant name')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='email address')),
                ('contact_number', models.CharField(max_length=15, verbose_name='contact number')),
                ('api_key', models.CharField(db_index=True, max_length=255, verbose_name='API key')),
                ('secret_key', models.CharField(db_index=True, max_length=255, verbose_name='secret key')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('registration_date', models.DateTimeField(blank=True, editable=False, verbose_name='registration date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical merchant',
                'verbose_name_plural': 'historical merchants',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('version', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=255, verbose_name='merchant name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('contact_number', models.CharField(max_length=15, verbose_name='contact number')),
                ('api_key', models.CharField(max_length=255, unique=True, verbose_name='API key')),
                ('secret_key', models.CharField(max_length=255, unique=True, verbose_name='secret key')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='registration date')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
