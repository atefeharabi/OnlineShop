from django.contrib import admin
from .models import Country, State, City


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)