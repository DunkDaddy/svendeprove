from django.db import models

# Create your models here.


class PostNummer(models.Model):
    postNr = models.IntegerField()
    byNavn = models.CharField(max_length=255, null=False)


class Person(models.Model):
    navn = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    tlf = models.IntegerField()
    postnummer = models.ForeignKey(PostNummer, on_delete=models.CASCADE)
    point = models.IntegerField()
    cpr = models.IntegerField()
    password = models.CharField(max_length=255)


class Handlinger(models.Model):
    handling = models.TextField()
    credit = models.IntegerField()

class Handling_Junctions(models.Model):
    handlingId = models.ForeignKey(Handlinger, on_delete=models.CASCADE)
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Rapport(models.Model):
    beskrivelse = models.TextField()
    tidspunkt = models.DateTimeField(auto_now=True)

class Rapport_junctions(models.Model):
    rapportId = models.ForeignKey(Rapport, on_delete=models.CASCADE)
    snitchId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='snitch')
    suspectId = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='suspect')

class PointGrade(models.Model):
    grade = models.CharField(max_length=10)
    minScore = models.IntegerField()
    maxScore = models.IntegerField()

class Permissions(models.Model):
    permissionsNavn = models.CharField(max_length=255)
    beskrivelse = models.TextField()

class Uddel_Permissions(models.Model):
    pointgradeId = models.ForeignKey(PointGrade, on_delete=models.CASCADE)
    permissionsId = models.ForeignKey(Permissions, on_delete=models.CASCADE)
