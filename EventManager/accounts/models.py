from django.db import models
from django import forms

# Create your models here.

class Event_Registration(models.Model):
    event_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    starting_date = models.DateTimeField(null=True)
    ending_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    host_email = models.EmailField(null=True)
    host_password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.event_name


