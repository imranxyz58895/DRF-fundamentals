from django.db import models


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=200)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return f'{self.ename}'