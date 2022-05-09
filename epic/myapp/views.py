from .serializers import (ClientSerializers,
                          EmployeeAdminSerializers,
                          ContractSerializers,
                          EvenementSerializers)
from .permissions import (CustomClientPermissions,
                          CustomContractPermissions,
                          CustomEvenementPermissions,
                          CustomEmployeePermissions)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Client,  Contract, CustomEmployee, Evenement
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class EmployeeAPIView(viewsets.ModelViewSet):
    serializer_class = EmployeeAdminSerializers
    permission_classes = [CustomEmployeePermissions]

    def get_queryset(self):
        employee = CustomEmployee.objects.all()
        return employee

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ClientAPIView(viewsets.ModelViewSet):
    serializer_class = ClientSerializers
    permission_classes = [CustomClientPermissions]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['last_name', 'email']
    search_fields = ['last_name', 'email']

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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['client__last_name', 'client__email', 'amount', 'date_creation']
    search_fields = ['client__last_name', 'client__email', 'amount', 'date_creation']


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['contract__client__last_name', 'contract__client__email', 'date_event_begin']
    search_fields = ['contract__client__last_name', 'contract__client__email', 'date_event_begin']

    def get_queryset(self):
        evenement = Evenement.objects.all()
        return evenement

    def get_object(self):
        obj = get_object_or_404(Evenement, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj