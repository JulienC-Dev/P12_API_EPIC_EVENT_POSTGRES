from django.contrib import admin
from .models import (User, Client, Contract, Evenement)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'compagny',
                    'phone_number', 'date_creation', 'date_update', 'prospect')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'amount', 'date_creation', 'date_signature', 'status')


class EvenementAdmin(admin.ModelAdmin):
    list_display = ('user', 'contract', 'title', 'type', 'description', 'localisation',
                    'date_event_begin', 'date_event_end')


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Evenement, EvenementAdmin)