from django.urls import path
from basketapp.views import basket,add_basket,remove_basket

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='index'),
    path('add/<int:id_product>/', add_basket, name='add_basket'),
    path('remove/<int:id_product>/', remove_basket, name='remove_basket')
]
