from django.contrib import admin
from django.urls import path

app_name = 'admins'

from .views import index,admin_users_delete,admin_users_update ,admin_users_create,UserListView
    # admin_users

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', admin_users_create, name='admin_users_create'),
    path('user-update/<int:id>', admin_users_update, name='admin_users_update'),
    path('user-delete/<int:id>', admin_users_delete, name='admin_users_delete'),
]
