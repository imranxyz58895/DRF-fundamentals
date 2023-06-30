from . import models 

from django.contrib import admin
from django.contrib.auth.models import User, Group


@admin.register(models.Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']


admin.site.unregister(User)
admin.site.unregister(Group)