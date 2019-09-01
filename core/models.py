from django.db import models

# Create your models here.

NATIONS = (
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
    nominative = models.CharField()  # e.g. "_They_ read a book."
    accusative = models.CharField()  # e.g. "The wolf saw _them_."
    genitive = models.CharField()    # e.g. "The horse took _their_ apple."

    def __str__(self):
        return "{nom} / {acc} / {gen}".format(nom=self.nominative,
                                              acc=self.accusative,
                                              gen=self.genitive)

class Person(models.Model):
    name = models.CharField()
    nation = models.CharField(choices=NATION_CHOICES)
    pronouns = models.ForeignKey()

    def __str__(self):
        return "{name} ({nation})".format(name=self.name, nation=self.nation)


class SummitDate(models.Model):
    year = models.IntegerField()
    season = models.CharField(choices=SEASON_CHOICES)

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
    author = models.CharField()

    def __str__(self):
        return self.text


class WriteupSection(models.Model):
    notes = models.ManyToManyField(Notes)
    narrative = models.ForeignKey(Notes)

    def __str__(self):
        return self.notes


class Vision(models.Model):
    visionary = models.ForeignKey(Person)
    guide = models.ForeignKey(Person)
    date = models.ForeignKey(SummitDate)
    soul_statuses = models.ForeignKey(WriteupSection) # TODO: Make this more systematic.
    account = models.ForeignKey(WriteupSection)
    day_ritual = models.ForeignKey(WriteupSection)
    night_ritual = models.ForeignKey(WriteupSection)
    commentaries = models.ManyToManyField(Notes)
