# Generated by Django 5.0.6 on 2024-06-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_address_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_line',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]