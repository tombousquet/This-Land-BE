# Generated by Django 3.1.4 on 2020-12-18 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201216_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PointsOfInterest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TellYourStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TellYourStories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
