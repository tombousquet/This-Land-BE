# Generated by Django 3.1.5 on 2021-01-06 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210105_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='username',
        ),
        migrations.RemoveField(
            model_name='tellyourstory',
            name='username',
        ),
    ]