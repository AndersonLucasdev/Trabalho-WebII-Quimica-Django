from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('cadastrar/', views.criar_amostra, name='cadastrar_amostra'),
    path('mostrar/', views.detalhes_das_amostras, name='mostrar_amostras')
]