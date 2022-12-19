from django.db import models


class PolicyType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
