from email.policy import default

from django.db import models

from core.models.policy_type import PolicyType


class PolicyPlan(models.Model):
    policy_type = models.ForeignKey(PolicyType, on_delete=models.DO_NOTHING)
    insurer_code = models.CharField(max_length=20)
    tpa_code = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    minimum_life_coverage = models.FloatField(null=True, blank=True, help_text="Life Insurance Only")
    maximum_life_coverage = models.FloatField(null=True, blank=True, help_text="Life Insurance Only")
    free_cover_limit = models.FloatField(null=True, blank=True, help_text="Life Insurance Only")
    fixed_sum_insured = models.FloatField(null=True, blank=True, help_text="Life Insurance Only")
    multiple_of_salary = models.FloatField(null=True, blank=True, help_text="Life Insurance Only")

    def __str__(self):
        return str(self.policy_type)
