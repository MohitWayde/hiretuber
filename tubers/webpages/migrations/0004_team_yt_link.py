# Generated by Django 3.1.4 on 2021-01-28 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_auto_20210125_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.CharField(default='', max_length=255),
        ),
    ]
