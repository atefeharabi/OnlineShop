from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from .managers import CustomerManager
from core.models import Country, State, City


class Customer(AbstractBaseUser):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    # slug = models.SlugField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=11)
    date_of_birth = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True

    @property
    def is_staff(self):
        return self.is_admin


