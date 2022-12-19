from django.contrib import admin

from core.models.client import Client
from core.models.insurer_company import InsurerCompany
from core.models.policy import Policy
from core.models.policy_plan import PolicyPlan
from core.models.policy_type import PolicyType
from core.models.sub_policy import SubPolicy
from core.models.third_party_assistant import ThirdPartyAssistant


class SubPolicyInline(admin.StackedInline):
    model = SubPolicy
    extra = 0


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'insurer_company')
    inlines = [SubPolicyInline]


admin.site.register(Policy, PolicyAdmin)
admin.site.register(InsurerCompany)
admin.site.register(PolicyPlan)
admin.site.register(Client)
admin.site.register(ThirdPartyAssistant)
admin.site.register(PolicyType)
admin.site.register(SubPolicy)