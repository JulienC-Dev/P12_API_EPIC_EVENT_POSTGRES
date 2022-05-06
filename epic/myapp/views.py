from .serializers import ClientSerializers, EmployeeAdminSerializers, ContractSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import Client,  Contract, CustomEmployee


class EmployeeAPIView(viewsets.ModelViewSet):
    serializer_class = EmployeeAdminSerializers

    def get_queryset(self):
        employee = CustomEmployee.objects.all()
        return employee


class ClientAPIView(viewsets.ModelViewSet):
    serializer_class = ClientSerializers

    def get_queryset(self):
        client = Client.objects.all()
        return client


class ContractAPIView(viewsets.ModelViewSet):
    serializer_class = ContractSerializers

    def get_queryset(self):
        contract = Contract.objects.all()
        return contract

    # def get_object(self):
    #     print(self.kwargs)
    #     obj = get_object_or_404(Contract, pk=self.kwargs.get('pk'))
    #     return obj