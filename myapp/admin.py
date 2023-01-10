from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    list_display = ("name","id")[::-1]


@admin.register(Model2)
class Model2Admin(admin.ModelAdmin):
    list_display = ("name","id")[::-1]


@admin.register(Model3)
class Model3Admin(admin.ModelAdmin):
    list_display = ("name","id")[::-1]
