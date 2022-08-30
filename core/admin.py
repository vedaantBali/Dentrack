from django.contrib import admin
from . import models

# Register your models here.


class OrderAdmin(admin.TabularInline):
    model = models.Order

    readonly_fields = [
        "dentist",
        "items",
        "amount",
    ]


class CompanyAdmin(admin.ModelAdmin):
    model = models.Company

    inlines = [
        OrderAdmin,
    ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        current_company = request.resolver_match.kwargs["object_id"]

        if db_field.name == "orders":
            kwargs["queryset"] = models.Order.objects.filter(
                company__id=current_company
            )
        if db_field.name == "products":
            kwargs["queryset"] = models.ProductByCompany.objects.filter(
                maker__id=current_company
            )
        if db_field.name == "auctions":
            kwargs["queryset"] = models.Auction.objects.filter(
                companies__in=[current_company]
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(models.Dentist)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Product)
admin.site.register(models.Item)
admin.site.register(models.Inventory)
admin.site.register(models.Auction)
admin.site.register(models.ProductByCompany)
admin.site.register(models.AuctionHistory)
admin.site.register(models.Order)
admin.site.register(models.Contact)
