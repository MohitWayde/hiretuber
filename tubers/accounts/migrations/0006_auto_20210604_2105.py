# Generated by Django 3.1.7 on 2021-06-04 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210604_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 4, 21, 5, 58, 751296)),
        ),
    ]
