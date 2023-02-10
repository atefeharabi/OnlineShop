from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name', 'date_of_birth')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['confirm_password'] and cd['password'] and cd['confirm_password'] != cd['password']:
            raise ValidationError('Passwords is not match')
        return cd['password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="Change Password Using <a href=\"../password/\">This Link</a>")

    class Meta:
        model = User
        fields = ('email', 'phone', 'password', 'last_login', 'first_name', 'last_name', 'date_of_birth')


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    #
    # def clean_confirm_password(self):
    #     cd = self.cleaned_data
    #     if cd['confirm_password'] and cd['password'] and cd['confirm_password'] != cd['password']:
    #         raise ValidationError('Passwords is not match')
    #     return cd['password']


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()