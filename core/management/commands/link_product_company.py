from django.core.management import BaseCommand
from core import models


def handle_link_products():
    new_products = models.ProductByCompany.objects.all()

    for product in new_products:
        new_company = product.maker
        company = models.Company.objects.get(id=new_company.id)
        company.products.add(product)

class Command(BaseCommand):
    help = "Link ProductByCompany to Company"

    def handle(self, *args, **options):
        handle_link_products()
        return "Done"