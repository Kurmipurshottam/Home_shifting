# Generated by Django 5.0.4 on 2024-04-12 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0009_rename_dcontact_contacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Delivery_Contacts',
        ),
    ]
