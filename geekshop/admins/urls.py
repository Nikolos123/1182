from django.contrib import admin
from django.urls import path

app_name = 'admins'

from .views import index,UserDeleteView,UserUpdateView ,UserCreateView,UserListView,CategoryListView
    # admin_users , admin_users_create,admin_users_update,admin_users_delete

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('user-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

path('category/', CategoryListView.as_view(), name='admin_category'),
path('category-update/<int:pk>/', CategoryListView.as_view(), name='admin_category_update'),



]
