# Generated by Django 5.1.5 on 2025-02-07 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0122_charfield_null_choices'),
        ('netbox_ptov', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='gns3srv',
            new_name='GNS3Server',
        ),
    ]