from django.db import models

# Create your models here.


class Contact(models.Model):
    phone_number = models.IntegerField(blank=True, null=True)
    address_line_1 = models.CharField(max_length=32)
    address_line_2 = models.CharField(max_length=32)
    # city = models.TextChoices()
class Dentist(models.Model):
    name = models.CharField(max_length=32)

class Company(models.Model):
    name = models.CharField(max_length=32)
