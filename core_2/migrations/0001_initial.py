# Generated by Django 4.0.5 on 2022-06-29 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Double',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('double_value', models.IntegerField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 29, 18, 35, 44, 117143))),
            ],
        ),
    ]
