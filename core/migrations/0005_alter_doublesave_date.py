# Generated by Django 4.0.5 on 2022-06-27 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_doublesave_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doublesave',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 27, 0, 0, 23, 877322), null=True),
        ),
    ]
