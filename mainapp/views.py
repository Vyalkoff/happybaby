from django.shortcuts import render
from pathlib import Path
import json
from mainapp.models import Product, ProductCategory
from basketapp.models import BasketItem


def openfile(file_json):
    path_json = Path(__file__).resolve().parent.joinpath('fixture', file_json)
    with open(path_json, 'r', encoding='utf-8') as file:
        js_prod = json.load(file)
    return js_prod


mini_basket = openfile('basket.json')
insta = openfile('insta.json')


# Create your views here.
def index(request):
    product_new = Product.objects.filter(status='new')[:5]
    product_most = Product.objects.filter(status='most')[:5]
    product_sale = Product.objects.filter(status='sale')[:5]
    category = ProductCategory.objects.all()
    basket = BasketItem.get_basket(request.user)
    context = {
        'title': 'happybabby-Главная',
        'category': category,
        'basket': basket,
        "insta": insta,
        "product_new": product_new,
        "product_most": product_most,
        "product_sale": product_sale,

    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id):
    product = Product.objects.filter(category=category_id)
    category = ProductCategory.objects.all()
    current_category = ProductCategory.objects.get(pk=category_id)
    basket = BasketItem.get_basket(request.user)
    context = {
        'title': current_category,
        'category': category,
        'basket': basket,
        "insta": insta,
        "product": product,
        'current_category': current_category

    }
    return render(request, 'mainapp/products.html', context)


def product_all(request):
    product = Product.objects.filter(status='most')
    category = ProductCategory.objects.all()
    basket = BasketItem.get_basket(request.user)
    context = {
        'title': 'Популярные',
        'category': category,
        'basket': basket,
        "insta": insta,
        "product": product,
        'current_category': 'Популярные'

    }
    return render(request, 'mainapp/products.html', context)


def details_product(request):
    category = ProductCategory.objects.all()
    basket = BasketItem.get_basket(request.user)
    context = {
        'title': 'happybabby',
        'category': category,
        'basket': basket,
        "insta": insta,
    }
    return render(request, 'mainapp/product_details.html', context)
