# Generated by Django 4.0.5 on 2022-06-29 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_2', '0002_alter_double_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='double',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 29, 18, 38, 36, 561336)),
        ),
    ]
