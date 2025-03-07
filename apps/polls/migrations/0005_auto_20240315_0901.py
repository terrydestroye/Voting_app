# Generated by Django 3.2.16 on 2024-03-15 09:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_alter_anonymousvoter_ip_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnonymousVoter',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='voters',
            field=models.ManyToManyField(blank=True, related_name='voters', to=settings.AUTH_USER_MODEL),
        ),
    ]
