from django.urls import path
from .views import category

app_name = 'products'
urlpatterns = [
    path('', category, name='category'),
    path('<int:category_id>/', category, name='category'),

]
