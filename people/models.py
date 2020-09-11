from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
