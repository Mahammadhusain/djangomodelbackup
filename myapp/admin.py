from django.contrib import admin

# Register your models here.
from .models import Model1,Model2

@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    list_display = ("name","id")[::-1]


@admin.register(Model2)
class Model2Admin(admin.ModelAdmin):
    list_display = ("name","id")[::-1]
