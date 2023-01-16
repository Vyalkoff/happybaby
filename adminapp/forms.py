from django import forms
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from mainapp.models import Product, ProductCategory


class UserAdminRegisterForm(UserRegisterForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'avatar', 'email', 'password1', 'password2')
        widgets = {'avatar': forms.widgets.FileInput()}


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)


class CategoryAdminProfileForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name',)


class ProductAdminProfileForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'old_price', 'quantity', 'specification', 'status',)
