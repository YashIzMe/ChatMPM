# Generated by Django 3.1.7 on 2021-04-25 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210425_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='icon',
        ),
    ]
