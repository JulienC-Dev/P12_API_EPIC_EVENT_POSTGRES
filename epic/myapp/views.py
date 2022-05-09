from .serializers import (ClientSerializers,
                          EmployeeAdminSerializers,
                          ContractSerializers,
                          EvenementSerializers)
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import Client,  Contract, CustomEmployee, Evenement
from .permissions import CustomClientPermissions, CustomContractPermissions, CustomEvenementPermissions


class EmployeeAPIView(viewsets.ModelViewSet):
    serializer_class = EmployeeAdminSerializers
    # permission_classes = [CustomEmployeePermissions]

    def get_queryset(self):
        employee = CustomEmployee.objects.all()
        return employee

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ClientAPIView(viewsets.ModelViewSet):
    serializer_class = ClientSerializers
    permission_classes = [CustomClientPermissions]

    def get_queryset(self):
        client = Client.objects.all()
        return client

    def get_object(self):
        obj = get_object_or_404(Client, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class ContractAPIView(viewsets.ModelViewSet):
    serializer_class = ContractSerializers
    permission_classes = [CustomContractPermissions]

    def get_queryset(self):
        contract = Contract.objects.all()
        return contract

    def get_object(self):
        obj = get_object_or_404(Contract, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class EvenementAPIView(viewsets.ModelViewSet):
    serializer_class = EvenementSerializers
    permission_classes = [CustomEvenementPermissions]

    def get_queryset(self):
        evenement = Evenement.objects.all()
        return evenement

    def get_object(self):
        obj = get_object_or_404(Evenement, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj