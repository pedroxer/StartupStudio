import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from UserSystem.models import CustomUser


class EventTag(models.Model):
    tag_name = models.CharField(max_length=40)

    def __str__(self):
        return self.tag_name


class EventPage(models.Model):
    event_title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    start_date = models.DateField('start date')
    ending_date = models.DateField('ending date')
    entry_deadline = models.DateTimeField('entry deadline')
    event_organiser = models.CharField(max_length=60)
    event_text = models.TextField(max_length=2000)
    event_prize = models.CharField(max_length=200)
    event_image = models.CharField(max_length=300)
    event_tags = models.ManyToManyField(EventTag) #Tag Fields following Many to Many rules
    event_main_text_culling = models.IntegerField(  # providing minimal and max values for text Culling
        default=800,
        validators=[
            MaxValueValidator(800),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.event_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=4) <= self.pub_date <= now


class EventComment(models.Model):
    article = models.ForeignKey(EventPage, on_delete=models.CASCADE)
#    user_name = models.CharField(max_length=30)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=600)
    pub_time = models.DateTimeField('date published')


# Create your models here.