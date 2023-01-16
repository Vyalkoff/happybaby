from django.contrib import admin
from .models import BasketItem


# Register your models here.


class BasketAdmin(admin.TabularInline):
    model = BasketItem
    fields = ('product', 'add_datetime', 'quantity',)
    readonly_fields = ('add_datetime',)
    extra = 0
