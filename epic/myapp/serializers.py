from rest_framework import serializers
from .models import Client, Contract, Evenement, CustomEmployee
from django.utils import timezone as tz
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group


class EmployeeAdminSerializers(serializers.ModelSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        queryset= Group.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = CustomEmployee
        fields = ['id', 'password', 'username', 'email', 'last_name', 'is_staff', 'groups']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('is_active', 'is_staff')


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id',
                  'employee',
                  'first_name',
                  'last_name',
                  'email',
                  'compagny',
                  'phone_number',
                  'prospect']


def validate_date(date_signature):
    if date_signature < tz.now():
        raise ValidationError("Date cannot be in the past")


class ContractSerializers(serializers.ModelSerializer):

    date_creation = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M",
        read_only=True,
        required=False)

    date_signature = serializers.DateTimeField(
        validators=[validate_date],
        input_formats=["%d-%m-%Y %H:%M"],
        format="%d-%m-%Y %H:%M",
        required=False,
        )

    class Meta:
        model = Contract
        fields = ['contrat_id',
                  'client',
                  'name',
                  'amount',
                  'date_creation',
                  'date_signature',
                  'status']
        read_only_fields = ['contrat_id']

    def validate(self, attrs):
        instance = Contract(**attrs)
        instance.clean()
        return attrs


class EvenementSerializers(serializers.ModelSerializer):
    date_event_begin = serializers.DateTimeField(
        validators=[validate_date],
        input_formats=["%d-%m-%Y %H:%M"],
        format="%d-%m-%Y %H:%M",
        required=False,
    )
    date_event_end = serializers.DateTimeField(
        validators=[validate_date],
        input_formats=["%d-%m-%Y %H:%M"],
        format="%d-%m-%Y %H:%M",
        required=False,
    )
    evenenement_id = serializers.PrimaryKeyRelatedField(read_only=True, source='id')
    class Meta:
        model = Evenement
        fields = ['evenenement_id',
                  'contract',
                  'employee',
                  'title',
                  'type',
                  'description',
                  'ville',
                  'date_event_begin',
                  'date_event_end']

    def validate(self, attrs):
        instance = Evenement(**attrs)
        instance.clean()
        return attrs



