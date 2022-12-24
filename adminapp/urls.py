from django.urls import path
from .views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('category/', CategoryListView.as_view(), name='admins_category'),
    path('category-create/', CategoryCreateView.as_view(), name='admins_user_create'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(), name='admins_user_update'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admins_user_delete'),
    path('user-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_user_delete'),

]
