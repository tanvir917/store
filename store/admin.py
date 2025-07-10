from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price','inventory_status', 'collection_title', 'last_update']
    list_editable = ['unit_price']
    list_per_page = 10
    search_fields = ['title', 'description']
    list_select_related = ['collection']
    ordering = ['title', 'unit_price', 'inventory']

    @admin.display(ordering='inventory')
    def inventory_status(self, product: models.Product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    def collection_title(self, product: models.Product):
        return product.collection.title

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user__first_name', 'user__last_name', 'membership']
    list_editable = ['membership']
    list_select_related = ['user']
    search_fields = ['user__first_name', 'user__last_name', 'email']
    ordering = ['user__first_name', 'user__last_name']
    list_per_page = 10
    
admin.site.register(models.Collection)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'placed_at']
    search_fields = ['customer__first_name', 'customer__last_name', 'id']
    ordering = ['-placed_at']
    list_per_page = 10
