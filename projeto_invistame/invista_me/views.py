from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Investimento
from .forms import InvestimentoForm


# Create your views here.

def home(request):
    pessoa = {
        'nome': 'Diego',
        'idade': 31,
        'hobby': 'Programar',

    }
    return render(request, 'investimentos/minhahistoria.html', pessoa)


def contato(request):
    return HttpResponse('Estamos indo bem!')


def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # caso post
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)  # usando algo ja existente
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')


def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})


def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('tipoinvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }

    return render(request, 'investimentos/investimento.html', context=dados)


def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', context=dados)
