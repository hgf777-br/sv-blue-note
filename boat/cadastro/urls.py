from django.urls import path
from . import views


app_name = 'cadastro'
urlpatterns = [
    path('setor/', views.setor, name='setor'),
    path('setor/insert/', views.setor_insert, name='setor_insert'),
    path('setor/edit/<int:setor_id>', views.setor_edit, name='setor_edit'),
    path('setor/delete/<int:setor_id>', views.setor_delete, name='setor_delete'),
    path('servico/', views.servico, name='servico'),
    path('servico/insert/', views.servico_insert, name='servico_insert'),
    path('servico/edit/<int:servico_id>', views.servico_edit, name='servico_edit'),
    path('servico/delete/<int:servico_id>', views.servico_delete, name='servico_delete'),
    path('fornecedor/', views.fornecedor, name='fornecedor'),
    path('fornecedor/insert/', views.fornecedor_insert, name='fornecedor_insert'),
    path('fornecedor/edit/<int:fornecedor_id>', views.fornecedor_edit, name='fornecedor_edit'),
    path('fornecedor/delete/<int:fornecedor_id>', views.fornecedor_delete, name='fornecedor_delete'),
]