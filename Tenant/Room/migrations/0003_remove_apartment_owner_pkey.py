# Generated by Django 4.2.1 on 2023-10-03 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0002_apartment_owner_pkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='owner_pkey',
        ),
    ]