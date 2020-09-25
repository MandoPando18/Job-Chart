import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Company(models.Model):
    company_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    YES = 'YES'
    NO = 'NO'
    Y_N_CHOICES = [
        (1, 'Y'),
        (0, 'N'),
    ]

    response = models.IntegerField(
            choices=Y_N_CHOICES,
            default=0,
    )

    phoneinterview = models.IntegerField(
            choices=Y_N_CHOICES,
            default=0,
    )

    test = models.IntegerField(
            choices=Y_N_CHOICES,
            default=0,
    )

    offer = models.IntegerField(
            choices=Y_N_CHOICES,
            default=0,
    )

    denied = models.IntegerField(
            choices=Y_N_CHOICES,
            default=0,
    )


    def __str__(self):
        return self.company_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
