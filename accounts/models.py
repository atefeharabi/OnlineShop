from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from core.models import Country, State, City


class User(AbstractBaseUser, PermissionsMixin):
    """
        create User model for supporting customer users and admin users.
    """
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    # slug = models.SlugField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=11)
    date_of_birth = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # define a manager for User model
    objects = UserManager()

    # set email field as default authentication filed
    USERNAME_FIELD = 'email'

    # set required fields for createsuperuser statement
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


class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.CharField(max_length=255)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country}, {self.state}, {self.city}, {self.district}, {self.address}"