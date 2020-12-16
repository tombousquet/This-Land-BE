# Generated by Django 3.1.4 on 2020-12-16 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.TextField(max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('street_address', models.CharField(max_length=255, verbose_name='Street Address')),
                ('city', models.CharField(max_length=55, verbose_name='City')),
                ('state', models.CharField(max_length=25, verbose_name='State')),
                ('zip_code', models.CharField(max_length=5, verbose_name='Zip')),
                ('images', models.ImageField(null=True, upload_to='media/images/')),
                ('category', models.CharField(max_length=35)),
                ('date_created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Points_of_interest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Point_of_interest',
        ),
    ]
