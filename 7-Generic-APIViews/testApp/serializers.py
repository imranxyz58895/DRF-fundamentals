from . import models 
from rest_framework import serializers

class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'
