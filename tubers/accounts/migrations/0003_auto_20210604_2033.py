# Generated by Django 3.1.7 on 2021-06-04 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210604_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 4, 20, 33, 18, 338007)),
        ),
    ]
