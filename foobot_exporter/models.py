from django.db import models

class Device(models.Model):
    mac = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    userId = models.IntegerField(default=0)
    uuid = models.CharField(max_length=500)

