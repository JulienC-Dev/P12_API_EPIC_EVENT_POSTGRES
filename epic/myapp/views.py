from .serializers import ClientSerializers, EmployeeAdminSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import Client, CustomEmployee


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
