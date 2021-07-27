from django.db import models
from django.core.validators import *


# Create your models here.

class MakeCreate(models.Model):
    name = models.CharField(max_length=100, null=True, help_text='Enter a Make (e.g. Dodge)',
                            validators=[MinLengthValidator(2, "Make Must be greater than 1 character")])

    def __str__(self):
        return self.name


class AutosCreate(models.Model):
    nickname = models.CharField(max_length=100, null=True,
                                validators=[MinLengthValidator(2, "Nickname Must be greater than 1 character")])
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=200, null=True)
    make = models.ForeignKey(MakeCreate, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
