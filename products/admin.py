from django.contrib import admin
from .models import Product
from .models import Offer


# This class customizes the admin panel and determines how the data will be displayed
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stocks')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Register the model at admin panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
