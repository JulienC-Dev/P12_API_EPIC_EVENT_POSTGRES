from rest_framework import serializers
from .models import Client, CustomEmployee


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
            return


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'compagny',
                  'phone_number',
                  'prospect']


