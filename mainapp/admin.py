from django.contrib import admin
from .models import ProductCategory, Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'image', 'category', 'description', ('price', 'quantity'))
    readonly_fields = ('description',)
    ordering = ('name', 'price')
    search_fields = ('name',)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = 'name',


admin.site.register(ProductCategory, ProductCategoryAdmin)
