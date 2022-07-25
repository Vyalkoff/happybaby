from django.shortcuts import render
from pathlib import Path
import json
from mainapp.models import Product, ProductCategory


def openfile(file_json):
    path_json = Path(__file__).resolve().parent.joinpath('fixture', file_json)
    with open(path_json, 'r', encoding='utf-8') as file:
        js_prod = json.load(file)
    return js_prod


menu = openfile('menu.json')
mini_basket = openfile('basket.json')
insta = openfile('insta.json')


# Create your views here.
def index(request):
    product_new = Product.objects.filter(status='new')[:5]
    product_most = Product.objects.filter(status='most')[:5]
    product_sale = Product.objects.filter(status='sale')[:5]
    category = ProductCategory.objects.all()

    context = {
        'title': 'happybabby',
        'category': category,
        'mini_basket': mini_basket,
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
    context = {
        'title': 'happybabby',
        'category': category,
        'mini_basket': mini_basket,
        "insta": insta,
        "product": product,
        'current_category': current_category

    }
    return render(request, 'mainapp/products.html', context)


def details_product(request):
    category = ProductCategory.objects.all()
    context = {
        'title': 'happybabby',
        'category': category,
        'mini_basket': mini_basket,
        "insta": insta,
    }
    return render(request, 'mainapp/product_details.html', context)
