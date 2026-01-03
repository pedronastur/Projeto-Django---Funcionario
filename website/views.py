from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import Funcionario

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "website/lista.html"
    context_object_name = "funcionarios"

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "website/cria.html"
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = "__all__"
    template_name = "website/atualiza.html"
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "website/exclui.html"
    success_url = reverse_lazy("website:lista_funcionarios")
