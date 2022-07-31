from django.contrib import admin
from .models import ProductCategory, Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = 'name',


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductCategory, ProductCategoryAdmin)
