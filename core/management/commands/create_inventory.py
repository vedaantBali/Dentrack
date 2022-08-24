from django.core.management import BaseCommand
from core import models


def handle_new_inventories():
    new_dentists = models.Dentist.objects.filter(
        inventory=None
    )
    if new_dentists.count() == 0:
        print("No new dentists. Exiting...")
        return
    for dentist in new_dentists:
        new_inventory = models.Inventory.objects.create(
            owner=dentist
        )
        dentist.inventory = new_inventory
        dentist.save()
    print(f"Created new inventories for {new_dentists.count()} dentists.")


class Command(BaseCommand):
    help = "Create empty inventories for new Dentists"

    def handle(self, *args, **options):
        handle_new_inventories()
        return "Done"
