from pydoc import describe
from django.db import models

# Create your models here.


class Submission(models.Model):
    bot_name = models.CharField(max_length=35)
    owner_name = models.CharField(max_length=35)
    language_used = models.CharField(max_length=20)
    description = models.TextField()
    site = models.URLField(blank=True)
    invite_link = models.URLField()
    bot_id = models.CharField(max_length=18)
    approved = models.BooleanField()
    profile_url = models.URLField(blank=True)
    def __str__(self):
        return self.bot_name
