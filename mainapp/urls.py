from django.urls import path
from .views import products, details_product

app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='products'),


]
