# Generated by Django 3.2.16 on 2024-02-15 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0004_rename_student_id_candidate_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='election',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='position',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
