from . import models, serializers
from django.shortcuts import render
from rest_framework import generics # https://www.django-rest-framework.org/api-guide/generic-views/


class EmployeeListAPIView(generics.ListAPIView):
    # queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

    def get_queryset(self):
        queryset = models.Employee.objects.all()
        name = self.request.GET.get('name', None)

        if name is not None:
            queryset = queryset.filter(ename__icontains=name)
        return queryset

class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer