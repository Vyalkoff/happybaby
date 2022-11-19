from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.views import insta
from mainapp.models import ProductCategory, Product
from .models import BasketItem


# Create your views here.
def basket(request):
    category = ProductCategory.objects.all()
    basket = BasketItem.objects.all()
    context = {
        'title': 'Корзина',
        'category': category,
        'basket': basket,
        "insta": insta,

    }

    return render(request, 'basketapp/checkout.html', context)


def add_basket(request, id_product):
    product = get_object_or_404(Product, id=id_product)
    basket = BasketItem.get_basket(request.user, product).first()
    if not basket:
        basket = BasketItem(name=request.user, product=product)
    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_basket(request, id_product):
    basket = get_object_or_404(BasketItem, product=id_product)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
