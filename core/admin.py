from django.contrib import admin
from .models import Country, State, City


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('f_name', )}


class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('f_name', )}


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('f_name', )}


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)