from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите логин пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_phone', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите логин '
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя '
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию '
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email '
        self.fields['mobile_phone'].widget.attrs['placeholder'] = 'Введите номер телефона '
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'