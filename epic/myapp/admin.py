from django.contrib import admin
from .models import (Client, Contract, Evenement, CustomEmployee)
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Groups'
    UserAdmin.list_display = ('username', 'email', 'is_active',
                              'date_joined', 'is_staff', 'group')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'compagny',
                    'phone_number', 'date_creation', 'date_update', 'prospect')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'amount', 'date_creation', 'date_signature', 'status')


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('contract', 'employee', 'title', 'type', 'description', 'localisation',
                    'date_event_begin', 'date_event_end')


# admin.site.unregister(User)
admin.site.register(CustomEmployee, CustomUserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Evenement, EvenementAdmin)