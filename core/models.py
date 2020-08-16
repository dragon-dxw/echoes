from django.db import models

# Create your models here.
from django.db.models import TextField, CharField, ForeignKey


class Volume(models.Model):
    date = CharField(max_length=100)

    def __str__(self):
        return self.date

class Vision(models.Model):
    account = TextField()
    volume = ForeignKey(Volume, on_delete=models.deletion.CASCADE)

    def __str__(self):
        """
        For now, use the first line of the vision text.
        """
        return str(self.account).split("\n")[0]