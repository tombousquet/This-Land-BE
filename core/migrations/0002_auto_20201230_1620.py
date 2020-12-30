# Generated by Django 3.1.4 on 2020-12-30 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PointsOfInterest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tellyourstory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TellYourStories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tellyourstory',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='tellyourstory',
            name='text',
            field=models.TextField(max_length=255, null=True),
        ),
    ]