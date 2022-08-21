from django.contrib import admin
from . import models
# Register your models here.


class DentistAdmin(admin.StackedInline):
    model = models.Dentist


class CompanyAdmin(admin.StackedInline):
    model = models.Company


class ContactAdmin(admin.ModelAdmin):
    inlines = [DentistAdmin, CompanyAdmin]


admin.site.register(models.Dentist)
admin.site.register(models.Company)
admin.site.register(models.Product)
admin.site.register(models.Contact, ContactAdmin)
