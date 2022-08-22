from django.db import models
from django.conf import settings
from . import constants
from django.core.validators import MinLengthValidator, EmailValidator


class Contact(models.Model):
    cities = []
    states = []
    for state in constants.STATE_MAP:
        for city in constants.STATE_MAP[state]:
            cities.append((city, city))
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

    def __str__(self) -> str:
        return self.email_id


class Inventory(models.Model):
    owner = models.OneToOneField(
        'Dentist', on_delete=models.DO_NOTHING, related_name='owner')
    items = models.ManyToManyField('Item')

    def __str__(self) -> str:
        return f'inventory_{self.owner}'


class Dentist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=32)
    contact = models.OneToOneField(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    inventory = models.OneToOneField(
        Inventory, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=32)
    contact = models.OneToOneField(
        Contact, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    products = models.ManyToManyField('Product')

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    product = models.OneToOneField('Product', on_delete=models.DO_NOTHING)
    count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.product}_{self.count}_nos'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False)
    list_price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    unit = models.CharField(
        max_length=16, choices=constants.UNITS, blank=False)
    maker = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.name}_{self.maker}'
