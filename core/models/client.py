from django.db import models

from core.models.sub_office import SubOffice


class Client(models.Model):
    arabic_name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)
    sub_office = models.ForeignKey(SubOffice, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.english_name
