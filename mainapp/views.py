from django.shortcuts import render
from pathlib import Path
import json


def openfile(file_json):
    path_json = Path(__file__).resolve().parent.joinpath('fixture', file_json)
    with open(path_json, 'r', encoding='utf-8') as file:
        js_prod = json.load(file)
    return js_prod


menu = openfile('menu.json')
mini_basket = openfile('basket.json')
insta = openfile('insta.json')
product = openfile('products.json')


# Create your views here.
def index(request):
    context = {
        'title': 'happybabby',
        'category': menu,
        'mini_basket': mini_basket,
        "insta": insta,
        "product": product,

    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'happybabby',
        'category': menu,
        'mini_basket': mini_basket,
        "insta": insta,

    }
    return render(request, 'mainapp/products.html', context)


def details_product(request):
    context = {
        'title': 'happybabby',
        'category': menu,
        'mini_basket': mini_basket,
        "insta": insta,
    }
    return render(request, 'mainapp/product_details.html', context)
