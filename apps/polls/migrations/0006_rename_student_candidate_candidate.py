# Generated by Django 3.2.16 on 2024-03-15 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20240315_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='student',
            new_name='candidate',
        ),
    ]
