from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.user + str(self.id)
