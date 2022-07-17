from django.shortcuts import render
import json
import os

path_menu = os.path.join(os.path.abspath('fixture'), 'menu.json')

with open(r'D:\happybaby\mainapp\fixture\menu.json', encoding='utf-8') as file:
    menu = json.load(file)



# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', context=menu)


def products(request):
    return render(request, 'mainapp/products.html',context=menu)


def details_product(request):
    return render(request, 'mainapp/product_details.html',context=menu)
