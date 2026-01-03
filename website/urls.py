from django.urls import path
from .views import (
    FuncionarioListView,
    FuncionarioCreateView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)

app_name = "website"

urlpatterns = [
    path("", FuncionarioListView.as_view(), name="lista_funcionarios"),
    path("cadastrar/", FuncionarioCreateView.as_view(), name="cadastra_funcionario"),
    path("editar/<int:pk>/", FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),
    path("excluir/<int:pk>/", FuncionarioDeleteView.as_view(), name="deleta_funcionario"),
]
