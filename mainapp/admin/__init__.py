from django.contrib import admin
from mainapp.models import *

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['part_number']
    search_fields = ['part_number', 'description']

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']
