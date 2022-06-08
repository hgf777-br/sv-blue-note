from django.urls import path
from . import views


app_name = 'manutencao'
urlpatterns = [
    path('lista/', views.lista, name='lista'),
]