# Generated by Django 4.0.1 on 2022-05-07 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsFeed', '0006_newsarticle_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]