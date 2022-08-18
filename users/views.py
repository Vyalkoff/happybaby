from django.shortcuts import render
from mainapp.models import ProductCategory
from mainapp.views import openfile
from users.forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect

mini_basket = openfile('basket.json')
insta = openfile('insta.json')
category = ProductCategory.objects.all()


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    else:
        form = UserLoginForm()
    context = {
        'title': 'happybabby-login',
        'category': category,
        'mini_basket': mini_basket,
        "insta": insta,
        "form": form,

    }
    return render(request, 'users/sing_in.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'title': 'happybabby-login',
        'category': category,
        'mini_basket': mini_basket,
        "insta": insta,
        "form": form,

    }
    return render(request, 'users/register.html', context)
