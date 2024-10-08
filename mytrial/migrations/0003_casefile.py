# Generated by Django 5.0.7 on 2024-08-09 10:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytrial', '0002_profile_is_verified'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.CharField(max_length=100)),
                ('postal_address', models.CharField(max_length=255)),
                ('telephone_number', models.CharField(max_length=15)),
                ('landlord_name', models.CharField(max_length=100)),
                ('agent', models.CharField(blank=True, max_length=100)),
                ('caretaker', models.CharField(blank=True, max_length=100)),
                ('auctioneer', models.CharField(blank=True, max_length=100)),
                ('duration_of_stay', models.CharField(blank=True, max_length=100)),
                ('monthly_rent', models.CharField(blank=True, max_length=100)),
                ('year_of_entry', models.CharField(blank=True, max_length=100)),
                ('deposit_paid', models.CharField(blank=True, max_length=100)),
                ('cause_of_action', models.CharField(blank=True, max_length=255)),
                ('problem', models.TextField(blank=True)),
                ('ocs_police_station', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('completed', 'Completed')], default='in_progress', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
