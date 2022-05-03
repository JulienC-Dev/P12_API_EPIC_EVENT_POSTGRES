from django.contrib import admin
from .models import (Client, Contract, Evenement)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'compagny',
                    'phone_number', 'date_creation', 'date_update', 'prospect')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'amount', 'date_creation', 'date_signature', 'status')


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('contract', 'title', 'type', 'description', 'localisation',
                    'date_event_begin', 'date_event_end')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Evenement, EvenementAdmin)