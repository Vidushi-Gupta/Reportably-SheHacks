# Generated by Django 3.1.3 on 2021-03-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_report_uniqueid'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='document',
            field=models.FileField(default=1, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
