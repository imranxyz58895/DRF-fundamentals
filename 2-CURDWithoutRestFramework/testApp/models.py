from django.db import models


class Employee(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=64)
    salary = models.FloatField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

