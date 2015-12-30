from django.db import models


class Query(models.Model):
    user = models.CharField(max_length=30)
    session = models.ForeignKey('session.Session')
    date = models.DateTimeField()
    query = models.CharField(max_length=500)
    result = models.IntegerField()

    # def __unicode__(self):
    #     return self.query[0:20]
