from pydoc import describe
from django.db import models

# Create your models here.


class Submission(models.Model):
    bot_name = models.CharField(max_length=35)
    owner_name = models.CharField(max_length=35)
    language_used = models.CharField(max_length=20)
    description = models.TextField()
    site = models.URLField()
    invite_link = models.URLField()
    bot_id = models.CharField(max_length=18)
