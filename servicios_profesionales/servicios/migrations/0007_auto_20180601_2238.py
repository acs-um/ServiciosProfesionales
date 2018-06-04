# Generated by Django 2.0.5 on 2018-06-01 22:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0006_service_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='users',
        ),
        migrations.AddField(
            model_name='service',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
