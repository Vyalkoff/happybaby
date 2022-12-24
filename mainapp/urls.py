from django.urls import path
from .views import product_all,products

app_name = 'products'
urlpatterns = [
    path('', product_all, name='product_all'),
    path('<int:category_id>/', products, name='products'),

]
