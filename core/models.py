from django.db import models

# Create your models here.

NATIONS = (
    # Imperial nations
    "the Brass Coast",
    "Dawn",
    "Highguard",
    "Imperial Orcs",
    "the League",
    "the Marches",
    "Navarr",
    "Urizen",
    "Varushka",
    "Wintermark",
    # Plus any foreigners we've had visionaries or guides from so far.
    "Faraden",
)
NATION_CHOICES = tuple((n, n) for n in NATIONS)

SEASONS = (
    "Spring",
    "Summer",
    "Autumn",
    "Winter",
)
SEASON_CHOICES = tuple((s, s) for s in SEASONS)

class Pronouns(models.Model):
    """Pronouns to use when referring to a visionary or guide.
    I'm using the case names we used for Latin and Greek because reasons."""
    nominative = models.CharField(max_length=50)  # e.g. "_They_ read a book."
    accusative = models.CharField(max_length=50)  # e.g. "The wolf saw _them_."
    genitive = models.CharField(max_length=50)    # e.g. "The horse took _their_ apple."

    def __str__(self):
        return "{nom} / {acc} / {gen}".format(nom=self.nominative,
                                              acc=self.accusative,
                                              gen=self.genitive)

class Person(models.Model):
    name = models.CharField(max_length=100)
    nation = models.CharField(max_length=100, choices=NATION_CHOICES)
    pronouns = models.ForeignKey(Pronouns, on_delete=models.PROTECT)

    def __str__(self):
        return "{name} ({nation})".format(name=self.name, nation=self.nation)


class SummitDate(models.Model):
    year = models.IntegerField()
    season = models.CharField(max_length=20, choices=SEASON_CHOICES)

    def __str__(self):
        if self.season in ("Spring", "Autumn"):
            festival = "Equinox"
        else:
            festival = "Solstice"
        return "{season} {festival} {year} YE".format(season=self.season,
                                                      festival=festival,
                                                      year=self.year)


class Notes(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    # TODO: Tie self.author into an actual Author model, optionally connected to User?

    def __str__(self):
        return self.text


class WriteupSection(models.Model):
    notes = models.ManyToManyField(Notes, related_name="section_for_notes")
    narrative = models.ForeignKey(Notes, on_delete=models.PROTECT, related_name="section_for_narrative")

    def __str__(self):
        return self.notes


class Vision(models.Model):
    visionary = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="visions_as_visionary")
    guide = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="visions_as_guide")
    date = models.ForeignKey(SummitDate, on_delete=models.PROTECT)
    soul_statuses = models.OneToOneField(WriteupSection, on_delete=models.PROTECT,
                                         related_name="vision_for_soul_statuses") # TODO: Make this more systematic.
    account = models.OneToOneField(WriteupSection, on_delete=models.PROTECT, related_name="vision_for_account")
    day_ritual = models.OneToOneField(WriteupSection, on_delete=models.PROTECT,
                                      related_name="vision_for_day_ritual")
    night_ritual = models.OneToOneField(WriteupSection, on_delete=models.PROTECT,
                                        related_name="vision_for_night_ritual")
    commentaries = models.ManyToManyField(Notes, related_name="vision_for_commentaries")
