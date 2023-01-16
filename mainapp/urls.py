from django.urls import path
from .views import CategoryView,CategoryAllView,ProductDetailView


app_name = 'products'
urlpatterns = [
    path('', CategoryAllView.as_view(), name='category_all'),
    path('<int:category_id>/', CategoryView.as_view(), name='category'),
    path('<int:category_id>/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),


]
