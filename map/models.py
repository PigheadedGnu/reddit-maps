from django.db import models

from project import sqlite_fields


class Map(models.Model):
    title = models.CharField(max_length=255)


class Submission(models.Model):
    reddit_id = models.CharField(max_length=255)
    url = models.URLField()
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    data = sqlite_fields.JSONField(blank=True)
    map = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}:{self.reddit_id}'
