# Generated by Django 2.1 on 2020-03-13 13:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 13, 2, 20, 848111, tzinfo=utc)),
        ),
    ]
