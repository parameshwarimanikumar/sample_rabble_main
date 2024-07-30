# Generated by Django 5.0.6 on 2024-06-12 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('userprofile', '0002_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='userprofile.profile'),
        ),
    ]
