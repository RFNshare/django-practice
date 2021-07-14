from django.db import models


# Create your models here.

class MakeCreate(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class AutosCreate(models.Model):
    nickname = models.CharField(max_length=100, null=True)
    mileage = models.IntegerField()
    comments = models.CharField(max_length=200, null=True)
    make = models.ForeignKey(MakeCreate, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
