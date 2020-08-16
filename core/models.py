from django.db import models

# Create your models here.
from django.db.models import TextField, CharField, ForeignKey


class Volume(models.Model):
    date = CharField(max_length=100)

class Vision(models.Model):
    account = TextField()
    volume = ForeignKey(Volume, on_delete=models.deletion.CASCADE)
