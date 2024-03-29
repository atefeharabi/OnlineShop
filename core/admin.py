from django.contrib import admin
from .models import Country, State, City, OtpCode


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'created')