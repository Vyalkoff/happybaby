from django.shortcuts import render
from pathlib import Path
import json
from mainapp.models import Product, ProductCategory
from basketapp.models import BasketItem
from django.views.generic import ListView, DetailView
from happybaby.mixin import TitleContextMixin


def openfile(file_json):
    path_json = Path(__file__).resolve().parent.joinpath('fixture', file_json)
    with open(path_json, 'r', encoding='utf-8') as file:
        js_prod = json.load(file)
    return js_prod


insta = openfile('insta.json')


# Create your views here.
class IndexView(ListView, TitleContextMixin):
    template_name = 'mainapp/index.html'
    model = BasketItem
    title = 'Главная'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['product_new'] = Product.objects.filter(status='new')[:5]
        context['product_most'] = Product.objects.filter(status='most')[:5]
        context['product_sale'] = Product.objects.filter(status='sale')[:5]
        context['insta'] = openfile('insta.json')
        context['basket'] = BasketItem.objects.filter(
            name=self.request.user) if self.request.user.is_authenticated else ''
        return context


class CategoryAllView(ListView, TitleContextMixin):
    model = ProductCategory
    template_name = 'mainapp/products.html'
    paginate_by = 4
    queryset = Product.objects.all()
    context_object_name = 'product'
    title = 'Все Товары'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryAllView, self).get_context_data(**kwargs)
        context['basket'] = BasketItem.get_basket(self.request.user)
        context['category'] = ProductCategory.objects.all()
        context['insta'] = openfile('insta.json')

        return context


class CategoryView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    paginate_by = 2
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['basket'] = BasketItem.get_basket(self.request.user)
        context['category'] = ProductCategory.objects.all()
        context['insta'] = openfile('insta.json')
        context['current_category'] = ProductCategory.objects.get(id=self.kwargs['category_id'])

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/product_details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['basket'] = BasketItem.get_basket(self.request.user)
        context['category'] = ProductCategory.objects.all()
        context['insta'] = openfile('insta.json')
        context['current_category'] = ProductCategory.objects.filter(id=self.kwargs['category_id'])

        return context


def details_product(request):
    category_all = ProductCategory.objects.all()
    basket = BasketItem.get_basket(request.user)
    context = {
        'title': 'happybabby',
        'category': category_all,
        'basket': basket,
        "insta": insta,
    }
    return render(request, 'mainapp/product_details.html', context)
