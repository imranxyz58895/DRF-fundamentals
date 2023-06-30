from . import models, serializers
from django.shortcuts import render 
from rest_framework import generics, mixins


class EmployeeListCreateModelMixin(generics.CreateAPIView, mixins.ListModelMixin):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class EmployeeRetrieveUpdateDestroyModelMixin(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # Retrieve
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)