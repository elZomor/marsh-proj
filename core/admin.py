from django.contrib import admin

from core.models.client import Client
from core.models.insurer_company import InsurerCompany
from core.models.policy import Policy
from core.models.policy_plan import PolicyPlan
from core.models.policy_type import PolicyType


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'insurer_company', 'is_sub_policy', 'parent')

    def is_sub_policy(self, obj):
        return 'YES' if obj.parent is not None else 'NO'


admin.site.register(Policy, PolicyAdmin)
admin.site.register(InsurerCompany)
admin.site.register(PolicyPlan)
admin.site.register(Client)
admin.site.register(PolicyType)
