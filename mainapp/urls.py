from django.urls import path
from .views import products, product_all

app_name = 'products'
urlpatterns = [
    path('', product_all, name='product_all'),
    path('<int:category_id>/', products, name='products'),

]
