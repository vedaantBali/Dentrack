from django.core.management import BaseCommand
from django.contrib.auth.models import User
from core import models
from core.management.commands.create_inventory import handle_new_inventories


def handle_link_users():
    users = User.objects.all()
    for user in users:
        if user.username.startswith("company"):
            try:
                models.Company.objects.create(
                    user=user,
                    name=user.username,
                    contact=models.Contact.objects.get(email_id=user.email),
                )
            except:
                pass
        if user.username.startswith("dentist"):
            try:
                models.Dentist.objects.create(
                    user=user,
                    name=user.username,
                    contact=models.Contact.objects.get(email_id=user.email),
                )
            except:
                pass


def handle_give_permissions():
    for i in range(0, 5):
        dentist = User.objects.get(username=f"dentist{i+1}")
        dentist.is_staff = True
        dentist.is_admin = True
        dentist.is_superuser = True
        dentist.save()
        company = User.objects.get(username=f"company{i+1}")
        company.is_staff = True
        company.is_admin = True
        company.is_superuser = True
        company.save()
        try:
            models.Contact.objects.create(
                phone_number=f"888888880{i+1}",
                email_id=f"{dentist.email}",
                address_line_1="address line 1",
                address_line_2="address line 2",
                city="Port Blair",
                state="Andaman & Nicobar Islands",
                pin_code="123456",
            )
        except:
            pass
        try:
            models.Contact.objects.create(
                phone_number=f"999999990{i+1}",
                email_id=f"{company.email}",
                address_line_1="address line 1",
                address_line_2="address line 2",
                city="Port Blair",
                state="Andaman & Nicobar Islands",
                pin_code="123456",
            )
        except:
            pass


def handle_create_users():
    for i in range(0, 5):
        try:
            User.objects.create(
                username=f"dentist{i+1}",
                email=f"dentist{i+1}@dentrack.com",
                password="password",
            )
        except:
            pass
        try:
            User.objects.create(
                username=f"company{i+1}",
                email=f"company{i+1}@dentrack.com",
                password="password",
            )
        except:
            pass


class Command(BaseCommand):
    help = "Setup database with new users"

    def handle(self, *args, **options):
        handle_create_users()
        handle_give_permissions()
        handle_link_users()
        handle_new_inventories()
        return "Done."
