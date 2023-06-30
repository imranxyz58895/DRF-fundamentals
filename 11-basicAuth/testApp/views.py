from django.shortcuts import render
from rest_framework import viewsets, permissions, authentication
from . import models, serializers

class EmployeeCURD(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    authentication_classes = [authentication.BasicAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]
