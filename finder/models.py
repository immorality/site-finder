from __future__ import unicode_literals

from django.contrib.admin import models
from django.db import models

class Site(models.Model):
    website = models.URLField(null=False)
    def __unicode__(self):
        return self.website

class Tag(models.Model):
    word = models.CharField(max_length=15, null=False)

    def __unicode__(self):
        return self.word

class Matches(models.Model):
    matching = models.ManyToManyField(Site)
    tags = models.ManyToManyField(Tag)


