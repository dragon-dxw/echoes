from django.db import models
from django.db.models import TextField, CharField, ForeignKey, IntegerField, BooleanField, UniqueConstraint

from sortedm2m.fields import SortedManyToManyField

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


class Writer(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Vision(models.Model):
    account = TextField()
    visionary = CharField(max_length=200)
    guide = CharField(max_length=200)
    dose_origin = CharField(max_length=300, blank=True, null=True)
    soul_status = TextField(blank=True, null=True)
    ritual_results = TextField(blank=True, null=True)
    commentary = TextField(blank=True, null=True)
    volume = ForeignKey(Volume, on_delete=models.deletion.CASCADE)
    order_in_volume = IntegerField()
    ready_to_publish = BooleanField(default=False)
    # ====
    notes_attribution = CharField(max_length=500, blank=True, null=True)
    account_attribution = CharField(max_length=500, blank=True, null=True)
    commentary_attribution = CharField(max_length=500, blank=True, null=True)
    # ====
    notes_writers = SortedManyToManyField(Writer, related_name="notes_written_by")
    account_writers = SortedManyToManyField(Writer, related_name="accounts_written_by")
    commentary_writers = SortedManyToManyField(Writer, related_name="commentary_written_by", blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['volume', 'order_in_volume'], name='unique_volume_and_order')
        ]

    def __str__(self):
        """
        Use the visionary's name and nation, which we've extracted.
        """
        return self.visionary

    def plain_text_output(self):
        output = []
        if self.dose_origin:
            output.append(str(self.dose_origin))
        output.append(str(self.account))
        if self.soul_status:
            output.append(str(self.soul_status))
        if self.ritual_results:
            output.append(str(self.ritual_results))
        if self.commentary:
            output.append(str(self.commentary))
        return "\n\n".join(output)
