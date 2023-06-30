from django.contrib import admin
from . import models 
from django.contrib.auth.models import Group, User 

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(models.Celebrity)
class CelebrityModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'unique_no', 'name', 'net_worth', 'address']