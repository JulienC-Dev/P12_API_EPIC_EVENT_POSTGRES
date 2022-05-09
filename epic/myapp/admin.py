from django.contrib import admin
from .models import (Client, Contract, Evenement, CustomEmployee)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class CustomEmployeeAdmin(UserAdmin):
    model = CustomEmployee

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Groups'
    UserAdmin.list_display = ('id', 'username', 'email', 'is_active',
                              'date_joined', 'is_staff', 'group')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_staff',
                                       'groups')}),
    )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("user_permissions", "is_superuser", "is_active")
        self.fieldsets[2][1]["fields"] = ('is_staff', 'groups')
        form = super(CustomEmployeeAdmin, self).get_form(request, obj, **kwargs)
        return form


class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'employee_service_support', 'first_name', 'last_name', 'email', 'compagny',
                    'phone_number', 'date_creation', 'date_update', 'prospect')

    def employee_service_support(self, obj):
        return obj.employee

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True:
            return True
        if obj is not None and obj.employee == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True:
            return True
        if obj is not None and obj.employee == request.user:
            return True
        return False


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id_contract', 'id_client', 'name', 'amount', 'date_creation', 'date_signature', 'status')

    def id_contract(self, obj):
        return obj.contrat_id

    def id_client(self, obj):
        return obj.client

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True:
            return True
        if obj is not None and obj.client.employee == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True:
            return True
        if obj is not None and obj.client.employee == request.user:
            return True
        return False


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('id_evenement', 'id_contract', 'id_client', 'responsable_event', 'title', 'type', 'description', 'ville',
                    'date_event_begin', 'date_event_end')

    def id_client(self, obj):
        return obj.contract.client

    def id_evenement(self, obj):
        return obj.id

    def id_contract(self, obj):
        return obj.contract

    def responsable_event(self, obj):
        return obj.employee

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True:
            return True
        if obj is not None and obj.employee == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='groupe de gestion').exists() or request.user.is_superuser == True:
            return True
        if obj is not None and obj.employee == request.user:
            return True
        return False


admin.site.register(CustomEmployee, CustomEmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Evenement, EvenementAdmin)