# Generated by Django 3.1.3 on 2021-03-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210303_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
