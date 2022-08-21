from os import stat
from django.db import models
from . import constants
from django.core.validators import MinLengthValidator, EmailValidator
# Create your models here.


class Contact(models.Model):
    cities = []
    states = []
    for city in constants.CITIES:
        cities.append((city, city))
    for state in constants.STATE_MAP:
        states.append((state, state))

    phone_number = models.CharField(max_length=10, validators=[
        MinLengthValidator(10)
    ], null=True)
    email_id = models.CharField(max_length=128, null=True, validators=[
        EmailValidator()
    ])
    address_line_1 = models.CharField(max_length=32)
    address_line_2 = models.CharField(max_length=32, blank=True)
    city = models.CharField(choices=cities, max_length=64, null=True)
    state = models.CharField(choices=states, max_length=64, null=True)
    pin_code = models.CharField(max_length=6, validators=[
        MinLengthValidator(6)
    ], null=True)


class Dentist(models.Model):
    name = models.CharField(max_length=32)
    contact = models.OneToOneField(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=32)
    contact = models.OneToOneField(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name
