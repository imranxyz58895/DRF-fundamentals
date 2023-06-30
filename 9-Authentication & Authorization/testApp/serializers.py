from . import models
from rest_framework.serializers import ModelSerializer


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = models.Employee 
        fields = '__all__'
