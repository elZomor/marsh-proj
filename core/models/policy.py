import datetime

from django.db import models

from core.models.insurer_company import InsurerCompany
from core.models.policy_plan import PolicyPlan
from core.models.client import Client


class Policy(models.Model):
    MONTHLY = 0
    QUARTERLY = 1
    SEMI_ANNUALLY = 2
    ANNUALLY = 3
    BILLING_FREQUENCY = (
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly'),
        (SEMI_ANNUALLY, 'Semi-Annual'),
        (ANNUALLY, 'Annually')
    )
    insurer_company = models.ForeignKey(InsurerCompany, on_delete=models.DO_NOTHING)
    plans = models.ForeignKey(PolicyPlan)
    insurer_number = models.CharField(max_length=20, null=True, blank=True)
    tpa_number = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    start_date = models.DateField(default=datetime.datetime.today)
    end_date = models.DateField()
    billing_frequency = models.IntegerField(choices=BILLING_FREQUENCY, null=True, blank=True)
    billing_area = models.CharField(max_length=20, null=True, blank=True)
    billing_address = models.CharField(max_length=50)
    card_delivery_area = models.CharField(max_length=20, null=True, blank=True)
    card_delivery_address = models.CharField(max_length=50, null=True, blank=True)
    client_contact_person = models.CharField(max_length=20, null=True, blank=True)
    insurer_contact_person = models.CharField(max_length=20, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children')

    def __str__(self):
        return self.name if not self.parent else '{} -> {}'.format(self.parent, self.name)
