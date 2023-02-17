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
    readonly_fields = ('last_login',)

    fieldsets = (
        ('Main', {'fields': ('email', 'phone', 'first_name', 'last_name', 'password', 'date_of_birth')}),
        ('Permission', {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        ('Main', {'fields': ('email', 'phone', 'password', 'confirm_password', 'first_name', 'last_name',
         'date_of_birth')}),
        ('Permission', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )
    search_fields = ('email', 'phone', 'first_name', 'last_name')
    ordering = ('last_name', 'first_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True

        return form


class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'country', 'state', 'city', 'district', 'postal_code')
    ordering = ('country', 'state', 'city', 'district')
    list_filter = ('country', 'state', 'city')
    search_fields = ('customer',)


# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)

