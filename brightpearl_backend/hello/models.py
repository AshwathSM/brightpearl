from django.db import models

# Create your models here.


class Hello(models.Model):

    message = models.CharField(max_length=255)
