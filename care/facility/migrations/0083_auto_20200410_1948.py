# Generated by Django 2.2.11 on 2020-04-10 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0082_populate_patient_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambulance',
            old_name='owner_is_smart_phone',
            new_name='owner_has_smart_phone',
        ),
    ]