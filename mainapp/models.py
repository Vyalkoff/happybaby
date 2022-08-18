from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    class Kind(models.TextChoices):
        SALE = 'sale', 'Распродажа'
        NEW = 'new', 'Новинка'
        MOST = 'most', 'Популярно'
        __empty__ = 'Выберите если требуется'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(verbose_name='имя', max_length=128, unique=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2,
                                default=0)
    old_price = models.DecimalField(verbose_name='старая цена продукта', max_digits=8, decimal_places=2,
                                    default=0, blank=True)

    quantity = models.PositiveIntegerField(verbose_name='колличество на складе',
                                           default=0)

    specification = models.TextField(verbose_name='характеристика', blank=True)
    status = models.CharField(max_length=6, blank=True, choices=Kind.choices)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} ({self.category})'
