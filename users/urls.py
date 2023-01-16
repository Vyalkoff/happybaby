from django.urls import path
from .views import LogOut, ProfileFormView, HBLogIn, RegisterListView

app_name = 'users'
urlpatterns = [
    path('login/', HBLogIn.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile')

]
