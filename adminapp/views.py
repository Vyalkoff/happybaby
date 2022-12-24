from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from users.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.urls import reverse_lazy
from happybaby.mixin import CustomDispatchMixin
from django.contrib.auth.decorators import login_required
from mainapp.models import ProductCategory,Product


# Create your views here.
@login_required
def index(request):
    return render(request, 'adminapp/admin.html')


class UserListView(ListView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'АДМИН | Пользователи'
        return context


class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('adminapp:admins_user')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'АДМИН | Пользователи'
        return context


class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admins_user')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'АДМИН | Обновление пользователя'
        return context


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:admins_user')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CategoryListView(ListView, CustomDispatchMixin):
    pass

    # model = ProductCategory
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(CategoryListView, self).get_context_data(**kwargs)


class CategoryCreateView(CreateView, CustomDispatchMixin):
    pass


class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    pass


class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    pass


class ProductListView(ListView, CustomDispatchMixin):
    pass


class ProductCreateView(CreateView, CustomDispatchMixin):
    pass


class ProductUpdateView(UpdateView, CustomDispatchMixin):
    pass


class ProductDeleteView(DeleteView, CustomDispatchMixin):
    pass
