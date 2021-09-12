from django.db import models
from django.db.models import TextField, CharField, ForeignKey, IntegerField, BooleanField, UniqueConstraint

from sortedm2m.fields import SortedManyToManyField

class Writer(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


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
    main_contributor = ForeignKey(Writer, on_delete=models.deletion.CASCADE)

    @property
    def festival_type(self):
        if self.date_season in ("Spring", "Autumn"):
            return "Equinox"
        else:
            return "Solstice"

    @property
    def volume_date(self):
        return "{v.date_season} {v.festival_type} {v.date_year} YE".format(v=self)

    @property
    def volume_title(self):
        return "Volume {v.number}, {v.volume_date}".format(v=self)

    def writers_for_volume(self, writer_type):
        assert writer_type in ('notes', 'accounts', 'commentary')
        field_mappings = {'notes': 'notes_written_by',
                          'accounts': 'accounts_written_by',
                          'commentary': 'commentary_written_by'}
        return Writer.objects.filter(**{"{}__in".format(field_mappings[writer_type]): self.vision_set.all()}
                                     ).distinct()

    @property
    def list_of_visions(self):
        return self.vision_set.order_by('order_in_volume')

    def __str__(self):
        return self.volume_title


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

    def list_account(self):
        return self.account.split('\n') 

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
