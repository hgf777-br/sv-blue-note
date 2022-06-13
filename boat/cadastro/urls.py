from django.urls import path
from . import views


app_name = 'cadastro'
urlpatterns = [
    path('setor/', views.setor, name='setor'),
    path('setor/insert/', views.setor_insert, name='setor_insert'),
    path('setor/edit/<int:setor_id>', views.setor_edit, name='setor_edit'),
    path('setor/delete/<int:setor_id>', views.setor_delete, name='setor_delete'),
]