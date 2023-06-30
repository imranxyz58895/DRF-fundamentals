from . import models, serializers, custom_permissions, custom_authentications
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class EmployeeAdd(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class EmployeeCURD(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    # locally set authentication   
    # authentication_classes = [JWTAuthentication,]
    authentication_classes = [custom_authentications.CustomAuthentication,]
    permission_classes = [permissions.IsAuthenticated,]