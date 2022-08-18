from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


# Create your models here.
def validator_age(age):
    if age < 10:
        raise ValidationError('Надо быть старше 10', code='min_value')


class User(AbstractUser):
    class KindCity(models.TextChoices):
        AKTAU = 'AK', 'Актау'
        ALMATA = 'AL', 'Алматы'
        __empty__ = 'Выберите город'

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    mobile_phone = models.CharField(max_length=11, unique=True, verbose_name='Мобильный номер')
    country = models.CharField(max_length=11, blank=True, choices=KindCity.choices, verbose_name='Город')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес')
    age = models.PositiveIntegerField(verbose_name='Возраст', validators=[validator_age])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'