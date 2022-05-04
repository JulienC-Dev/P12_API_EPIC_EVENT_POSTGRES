from rest_framework import serializers
from .models import Client, CustomEmployee, Contract, Evenement


class EmployeeAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomEmployee
        fields = ['id', 'password', 'username', 'email', 'last_name', 'is_staff', 'groups']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        read_only_fields = ('is_active', 'is_staff')

        def create(self, validated_data):
            password = validated_data.pop("password", None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id',
                  'first_name',
                  'last_name',
                  'email',
                  'compagny',
                  'phone_number',
                  'prospect']


class ContractSerializers(serializers.ModelSerializer):

    date_creation = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M",
        read_only=True,
        required=False)

    date_signature = serializers.DateTimeField(
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

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        Evenement(contract=instance).save()
        return instance