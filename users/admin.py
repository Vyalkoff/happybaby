from django.contrib import admin
from .models import User
from basketapp.models import BasketItem
from basketapp.admin import BasketAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active',)
    model = BasketItem
    inlines = (BasketAdmin,)
