# Generated by Django 2.0.5 on 2018-06-11 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_myuser_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='service',
        ),
    ]