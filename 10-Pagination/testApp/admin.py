from django.contrib import admin
from . import models 


@admin.register(models.Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']
