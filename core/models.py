from django.db import models
from django.conf import settings
from . import constants, utils
from django.core.validators import MinLengthValidator, EmailValidator


class Contact(models.Model):
    cities, states = utils.get_cities_states()

    phone_number = models.CharField(
        max_length=10, validators=[MinLengthValidator(10)], null=True, unique=True
    )
    email_id = models.CharField(
        max_length=128, null=True, validators=[EmailValidator()], unique=True
    )
    address_line_1 = models.CharField(max_length=32)
    address_line_2 = models.CharField(max_length=32, blank=True)
    city = models.CharField(choices=cities, max_length=64, null=True)
    state = models.CharField(choices=states, max_length=64, null=True)
    pin_code = models.CharField(
        max_length=6, validators=[MinLengthValidator(6)], null=True
    )

    def __str__(self) -> str:
        return self.email_id


class Inventory(models.Model):
    owner = models.OneToOneField(
        "Dentist", on_delete=models.CASCADE, related_name="owner"
    )
    items = models.ManyToManyField("Item", blank=True)

    def __str__(self) -> str:
        return f"inventory_{self.owner}"


class Dentist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True
    )
    name = models.CharField(max_length=32)
    contact = models.OneToOneField(
        Contact, on_delete=models.CASCADE, blank=True, null=True
    )
    inventory = models.OneToOneField(
        Inventory, on_delete=models.CASCADE, null=True, blank=True
    )
    orders = models.ManyToManyField("Order", related_name="dentist_order", blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            new_inventory = Inventory.objects.create(
                owner=self,
            )
            self.inventory = new_inventory
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True
    )
    name = models.CharField(max_length=32)
    contact = models.OneToOneField(Contact, on_delete=models.DO_NOTHING, null=True)
    products = models.ManyToManyField("ProductByCompany", blank=True)
    auctions = models.ManyToManyField("Auction")
    orders = models.ManyToManyField("Order", related_name="company_order", blank=True)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    product = models.OneToOneField("ProductByCompany", on_delete=models.DO_NOTHING)
    count = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product}_{self.count}_nos"


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False)
    quantity = models.IntegerField(blank=False)
    unit = models.CharField(max_length=16, choices=constants.UNITS, blank=False)

    def __str__(self) -> str:
        return f"{self.name}_{self.quantity}_{self.unit}"


class ProductByCompany(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    maker = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    price = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        company = Company.objects.get(id=self.maker.id)
        company.products.add(self)

    def __str__(self) -> str:
        return f"{self.product}_{self.maker}"


class Auction(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.DO_NOTHING, null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=True)
    product_count = models.IntegerField()
    companies = models.ManyToManyField(Company)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    history = models.ManyToManyField(
        "AuctionHistory", blank=True, related_name="auction_history"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for company in self.companies.all():
            auction_participant = Company.objects.get(id=company.id)
            auction_participant.auctions.add(self)

    class Meta:
        unique_together = (
            "dentist",
            "product",
        )

    def __str__(self) -> str:
        if self.is_active:
            active = "active"
        else:
            active = "inactive"
        return f"{self.dentist}_{self.product}_{self.price}_{active}"


class AuctionHistory(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)
    bid_by = models.ForeignKey(Company, on_delete=models.CASCADE)
    bid_price = models.IntegerField()
    index = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_index = AuctionHistory.objects.filter(auction=self.auction).aggregate(
                largest=models.Max("index")
            )["largest"]
            if last_index is not None:
                self.index = last_index + 1
            else:
                self.index = 1
        if self.auction.price < self.bid_price:
            return "Bid price should be less than current price"
        auction = Auction.objects.get(id=self.auction.id)
        auction.price = self.bid_price
        auction.save()
        super().save(*args, **kwargs)
        auction.history.add(self)

    def __str__(self) -> str:
        return f"{self.index}_{self.auction}_{self.bid_by}_{self.bid_price}"


class Order(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    status = models.CharField(max_length=32, choices=constants.ORDER_STATUS, blank=True)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.dentist}_{self.company}_{self.status}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = constants.ORDER_STATUS[0][0]
        super().save(*args, **kwargs)
        order_company = Company.objects.get(id=self.company.id)
        order_company.orders.add(self)
        order_dentist = Dentist.objects.get(id=self.dentist.id)
        order_dentist.orders.add(self)
