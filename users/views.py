from django.utils.decorators import method_decorator
from django.views.generic import FormView, UpdateView
from basketapp.models import BasketItem
from mainapp.models import ProductCategory
from mainapp.views import openfile
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from happybaby.mixin import TitleContextMixin

insta = openfile('insta.json')


class HBLogIn(LoginView, TitleContextMixin):
    template_name = 'users/sing_in.html'
    form_class = UserLoginForm
    title = 'Авторизация'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['insta'] = insta
        context['basket'] = BasketItem.objects.filter(
            name=self.request.user) if self.request.user.is_authenticated else ''
        return context


class RegisterListView(FormView, TitleContextMixin):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    title = 'Регистрация'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Вы Успешно зарегестрировались')
        return reverse('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['insta'] = insta
        context['basket'] = BasketItem.objects.filter(
            name=self.request.user) if self.request.user.is_authenticated else ''
        return context


class LogOut(LoginRequiredMixin, LogoutView):
    next_page = 'index'


class ProfileFormView(UpdateView, TitleContextMixin, LoginRequiredMixin):
    form_class = UserProfileForm
    model = User
    title = 'Профиль'
    template_name = 'users/profile.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Данные сохранены')
        return reverse('users:profile')

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileFormView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['basket'] = BasketItem.objects.filter(
            name=self.request.user) if self.request.user.is_authenticated else ''
        context['insta'] = insta
        return context
