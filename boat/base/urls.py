from django.urls import path
from . import views


app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('list_user/', views.list_user, name='list_user'),
    path('list_user/delete_user/<int:user_id>', views.delete_user, name='delete_user'),
    path('list_user/edit_user/<int:user_id>', views.edit_user, name='edit_user'),
]