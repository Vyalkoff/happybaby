from django.db import models
from mainapp.models import Product
from users.models import User


# Create your models here.
class BasketItem(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Колличество', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now=True)

    @staticmethod
    def get_basket(user, product=False):
        if user.is_authenticated:
            if product:
                return BasketItem.objects.filter(name=user, product=product)
            else:
                return BasketItem.objects.filter(name=user)
        else:
            return []

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    @property
    def filter_user(self):
        return BasketItem.get_basket(self.name)

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        return sum(basket.sum() for basket in self.filter_user)

    def total_quantity(self):
        return sum(basket.quantity for basket in self.filter_user)
