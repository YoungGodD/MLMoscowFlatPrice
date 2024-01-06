from django.db import models


class Price(models.Model):
    name = models.CharField(max_length=15, default="name")
    totsp = models.IntegerField()
    livesp = models.IntegerField()
    kitsp = models.IntegerField()
    dist = models.IntegerField()
    metrdist = models.IntegerField()
    walk = models.BooleanField()
    brick = models.BooleanField()
    floor = models.BooleanField()

    def __str__(self) -> str:
        return self.name