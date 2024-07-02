from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Alarm)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'time', 'active']