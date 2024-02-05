from django.db import models

class Competition(models.Model):
    name = models.CharField(max_length=60, null=True)
    code = models.CharField(max_length=60, null=True)
    areaname = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=60, null=True)
    tla = models.CharField(max_length=60, null=True)
    shortname = models.CharField(max_length=60, null=True)
    areaname = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60, null=True)
    competition = models.ForeignKey(Competition, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=60, null=True)
    position = models.CharField(max_length=60, null=True)
    dateofbirth = models.CharField(max_length=60, null=True)
    countryofbirth = models.CharField(max_length=60, null=True)
    nationality = models.CharField(max_length=60, null=True)
    team = models.ForeignKey(Team, default="", on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
