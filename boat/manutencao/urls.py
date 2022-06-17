from django.urls import path
from . import views


app_name = 'manutencao'
urlpatterns = [
    path('realizado/', views.realizado, name='realizado'),
    path('insert/', views.evento_insert, name='evento_insert'),
    path('edit/<int:evento_id>', views.evento_edit, name='evento_edit'),
    path('delete/<int:evento_id>', views.evento_delete, name='evento_delete'),
]