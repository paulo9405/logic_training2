# Generated by Django 4.0.5 on 2022-06-27 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_doublesave_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doublesave',
            name='date',
        ),
    ]
