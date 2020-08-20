from django.db import models

# Create your models here.
from django.db.models import TextField, CharField, ForeignKey, IntegerField

SEASONS = (
    "Spring",
    "Summer",
    "Autumn",
    "Winter",
)
SEASON_CHOICES = tuple((s, s) for s in SEASONS)

class Volume(models.Model):
    number = CharField(max_length=10,
                       help_text="The volume number (e.g. 2a)")
    date_season = CharField(choices=SEASON_CHOICES,
                            max_length=6)
    date_year = IntegerField()

    @property
    def festival_type(self):
        if self.date_season in ("Spring", "Autumn"):
            return "Equinox"
        else:
            return "Solstice"

    @property
    def volume_title(self):
        return "Volume {v.number}, {v.date_season} {v.festival_type} {v.date_year} YE".format(v=self)

    def __str__(self):
        return self.volume_title

class Vision(models.Model):
    account = TextField()
    visionary = CharField(max_length=200)
    volume = ForeignKey(Volume, on_delete=models.deletion.CASCADE)

    def __str__(self):
        """
        Use the visionary's name and nation, which we've extracted.
        """
        return self.visionary
