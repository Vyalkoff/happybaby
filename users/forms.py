from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    error_messages = {'password_mismatch': 'Пароли не совпадают'}

    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию '
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email '
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('avatar', 'username', 'last_name', 'address', 'email',)
        labels = {'username': 'Имя', 'last_name': 'Фамилия',
                  'address': 'Адрес доставки',
                  'email': 'Email'}
        widgets = {'avatar': forms.widgets.FileInput()}
        help_texts = {'username': False}

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию '
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email '
        self.fields['address'].widget.attrs['placeholder'] = 'Введите адрес'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'

    def clean(self):
        errors = {}
        type_place = [self.cleaned_data['username'], self.cleaned_data['last_name']]
        for id, item in enumerate(type_place):
            if any(map(str.isdigit, item)):
                if not id:
                    errors['username'] = ValidationError(f'Недопустимые символы в {item}')
                else:
                    errors['last_name'] = ValidationError(f'Недопустимые символы в {item}')
        if errors:
            raise ValidationError(errors)

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data and data.size > 8 ** 6:
            raise ValidationError('Большой файл')
        return data
