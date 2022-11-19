from mainapp.models import ProductCategory
from mainapp.views import openfile
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login'))
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


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            print(form.errors)
            form.save()
            messages.success(request, 'Данные сохранены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Profile',
        'category': category,
        'mini_basket': mini_basket,
        "insta": insta,
        'form': form
    }
    return render(request, 'users/profile.html', context)
