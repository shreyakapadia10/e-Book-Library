# Generated by Django 2.2.5 on 2019-10-07 02:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190930_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 7, 2, 16, 50, 300042, tzinfo=utc)),
        ),
    ]
