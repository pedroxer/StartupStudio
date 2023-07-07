# Generated by Django 4.0.1 on 2022-05-15 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_project_project_end_project_project_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_end',
            field=models.DateField(verbose_name='Project Ending'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start',
            field=models.DateField(verbose_name='Project Start'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('pen', 'На рассмотрении'), ('acc', 'Принято'), ('den', 'Отклонено'), ('act', 'Активно'), ('fin', 'Завершено')], default='p', help_text='Current project status', max_length=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 15, 15, 52, 9, 90668, tzinfo=utc), verbose_name='Date Time published'),
        ),
    ]