# Generated by Django 3.1.3 on 2021-03-03 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='time',
            new_name='location',
        ),
    ]
