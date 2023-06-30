from . import models, serializers
from django.shortcuts import render
from rest_framework import generics, pagination
from .paginations import MyLimitPagination, MyPagination

class EmployeeAdd(generics.ListAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filterset_fields = ('ename', )

    # locally pagination
    # pagination_class = pagination.PageNumberPagination
    pagination_class = MyLimitPagination

    """
    # vanila filtering
    def get_queryset(self):
        queryset = models.Employee.objects.all()
        name = self.request.GET.get('name')

        if name is not None:
            queryset = models.Employee.objects.filter(ename__icontains=name)
        return queryset
    """
