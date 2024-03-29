# Generated by Django 3.1.7 on 2021-06-10 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0008_auto_20210604_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='YtResponseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ytmsg', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 15, 43, 8, 101693)),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='user',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
