from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('servico/', views.servico_api, name='servico_api'),
    
]