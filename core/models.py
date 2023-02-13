from datetime import timedelta, datetime
import pytz
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class OtpCode(models.Model):
    phone = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    @property
    def expired(self):
        return  datetime.now(tz=pytz.timezone('Asia/Tehran')) + timedelta(minutes=2)

    def __str__(self):
        return f"{self.phone} - {self.code} - {self.created}"

    def is_expired(self):
        if self.created < self.expired:
            return True
        else:
            return False
