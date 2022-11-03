from django.urls import path
from .views import products

app_name = 'products'
urlpatterns = [
    path('<int:category_id>/', products, name='products'),


]
