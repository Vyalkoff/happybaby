from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
    class KindCity(models.TextChoices):
        AKTAU = 'AK', 'Актау'
        ALMATA = 'AL', 'Алматы'
        __empty__ = 'Выберите город'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    country = models.CharField(max_length=11, blank=True, choices=KindCity.choices, verbose_name='Город')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
