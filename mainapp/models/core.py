from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
class Part(models.Model):
    part_number = models.CharField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    container = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Container", related_name="container_parts")
    def __str__(self):
        return str(self.id)

class Container(models.Model):
    name = models.CharField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    parent_container = models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, to="mainapp.Container", related_name="parent_container_containers")
    def __str__(self):
        return str(self.name)
