from django import forms
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserAdminRegisterForm(UserRegisterForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'avatar', 'email', 'password1', 'password2')
        widgets = {'avatar': forms.widgets.FileInput()}


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
