from django.contrib import admin

from connexto.cars.models import Cars


@admin.register(Cars)
class PetAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'slug')
