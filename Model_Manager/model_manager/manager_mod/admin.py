from django.contrib import admin
from .models import modmanager
# Register your models here.

@admin.register(modmanager)
class adm(admin.ModelAdmin):
    list_display = ['name','age','address']