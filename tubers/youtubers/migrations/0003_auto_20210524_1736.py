# Generated by Django 3.1.7 on 2021-05-24 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210524_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 24, 17, 36, 47, 605092)),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/ytubers/%Y/%m/'),
        ),
    ]
