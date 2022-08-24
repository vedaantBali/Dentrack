from django.db import models
from django.conf import settings
from . import constants, utils
from django.core.validators import MinLengthValidator, EmailValidator


class Contact(models.Model):
    cities, states = utils.get_cities_states()

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
    items = models.ManyToManyField('Item', blank=True)

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
    products = models.ManyToManyField('ProductByCompany', blank=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    product = models.OneToOneField('Product', on_delete=models.DO_NOTHING)
    count = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.product}_{self.count}_nos'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False)
    quantity = models.IntegerField(blank=False)
    unit = models.CharField(
        max_length=16, choices=constants.UNITS, blank=False)

    def __str__(self) -> str:
        return f'{self.name}_{self.quantity}_{self.unit}'


class ProductByCompany(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, null=True)
    maker = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.product}_{self.maker}'


class Auction(models.Model):
    dentist = models.ForeignKey(
        Dentist, on_delete=models.DO_NOTHING, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, null=True)
    companies = models.ManyToManyField(Company)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('dentist', 'product',)

    def __str__(self) -> str:
        if self.is_active:
            active = "active"
        else:
            active = "inactive"
        return f'{self.dentist}_{self.product}_{active}'
