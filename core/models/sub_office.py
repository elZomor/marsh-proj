from django.db import models


class SubOffice(models.Model):
    arabic_name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)

    def __str__(self):
        return self.english_name
