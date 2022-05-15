from django.urls import path
from .views import home, contato, criar, investimento_registrado, investimentos, detalhe, editar, excluir

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('novo_investimento/', criar, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>', excluir, name='excluir'),
    path('investimento_registrado/', investimento_registrado, name='investimento_registrado'),
    path('investimentos/', investimentos, name='investimentos'),
    path('investimentos/<int:id_investimento>', detalhe, name='detalhe')
]
