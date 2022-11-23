from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.template.loader import render_to_string

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


@login_required
def add_basket(request, id_product):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(
            reverse('products:products', args=[get_object_or_404(Product, id=id_product).category.id]))
    product = get_object_or_404(Product, id=id_product)
    basket = BasketItem.get_basket(request.user, product).first()
    if not basket:
        basket = BasketItem(name=request.user, product=product)
    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_basket(request, id_product):
    basket = BasketItem.objects.get(id=id_product)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_edit(request, id, quantity):
    if request.META.get('HTTP_X_REQUESTED_WITH') == "XMLHttpRequest":
        baskets = BasketItem.objects.get(id=id)
        if quantity > 0:
            baskets.quantity = quantity
            baskets.save()
        else:
            baskets.delete()
        baskets = BasketItem.objects.filter(name=request.user)
        context = {
            'basket': baskets
        }
        result = render_to_string('basketapp/basket_product.html', context)
        return JsonResponse({'result': result})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
