from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import Group
from .models import User, Address


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('Main', {'fields': ('email', 'phone', 'first_name', 'last_name', 'password', 'date_of_birth')}),
        ('Permission', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('email', 'phone', 'password', 'confirm_password', 'first_name', 'last_name',
         'date_of_birth')}),
        ('Permission', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )
    search_fields = ('email', 'phone', 'first_name', 'last_name')
    ordering = ('last_name', 'first_name', 'email')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Address)

