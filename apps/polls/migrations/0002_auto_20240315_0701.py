# Generated by Django 3.2.16 on 2024-03-15 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anonymousvoter',
            name='browser_info',
        ),
        migrations.RemoveField(
            model_name='anonymousvoter',
            name='ip_address',
        ),
    ]
