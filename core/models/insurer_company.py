from django.db import models


class InsurerCompany(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    tpa_name = models.CharField(max_length=100, null=True, blank=True)
    tpa_code = models.CharField(max_length=30, null=True, blank=True)
    tpa_address = models.CharField(max_length=100,null=True, blank=True)
    tpa_area = models.CharField(max_length=50, null=True, blank=True)
    TAT = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
