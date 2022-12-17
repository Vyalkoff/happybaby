from django.urls import path
from .views import index, UserListView,UserCreateView,UserUpdateView,UserDeleteView


app_name = 'adminapp'

urlpatterns =[
    path('',index, name='index'),
    path('users/',UserListView.as_view(),name='admins_user'),
    path('user-create/',UserCreateView.as_view(),name='admins_user_create'),
    path('user-update/<int:pk>/',UserUpdateView.as_view(),name='admins_user_update'),
    path('user-delete/<int:pk>/',UserDeleteView.as_view(),name='admins_user_delete'),

]