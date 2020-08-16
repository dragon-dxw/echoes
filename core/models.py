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
                       default="<not set>",
                       help_text="The volume number (e.g. 2a)")
    date_season = CharField(choices=SEASON_CHOICES,
                            max_length=6,
                            default="Winter")
    date_year = IntegerField(default=0)
    date = CharField(max_length=100)

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
    volume = ForeignKey(Volume, on_delete=models.deletion.CASCADE)

    def __str__(self):
        """
        For now, use the first line of the vision text.
        """
        return str(self.account).split("\n")[0]