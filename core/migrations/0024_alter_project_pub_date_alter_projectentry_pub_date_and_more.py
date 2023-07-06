# Generated by Django 4.0.1 on 2023-07-06 14:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_project_pub_date_alter_projectentry_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 14, 8, 58, 190219, tzinfo=utc), verbose_name='Date Time published'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 14, 8, 58, 197315, tzinfo=utc), verbose_name='Время, когда заяка была отправлена'),
        ),
        migrations.AlterField(
            model_name='projectentry',
            name='status_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 14, 8, 58, 197349, tzinfo=utc), verbose_name='Время, когда статус заявки был изменен'),
        ),
        migrations.AlterField(
            model_name='projectnotice',
            name='pub_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 14, 8, 58, 202671, tzinfo=utc)),
        ),
    ]