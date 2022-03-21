# Generated by Django 4.0.3 on 2022-03-21 20:20

from django.db import migrations
import django_celery_beat.models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crontabschedule',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(
                default=
                django_celery_beat.models.crontab_schedule_celery_timezone,
                help_text=
                'Timezone to Run the Cron Schedule on. Default is UTC.',
                use_pytz=False, verbose_name='Cron Timezone'),
        ),
    ]
