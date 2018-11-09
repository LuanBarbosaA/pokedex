from django.shortcuts import render
from .models import Pokemon
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404

# Create your views here.


def listar_todos(request):
    # todos os objetos do DB.
    pokemons_list = Pokemon.objects.all().order_by('-nome')
    # abaixo, para saber QUANTAS páginas devem aparecer
    paginator = Paginator(pokemons_list, 3)
    # abaixo, pega qual página o usuário esta
    page = request.GET.get('page')
    # abaixo, pega quais os registros são desta página
    pokemons = paginator.get_page(page)

    contexto = {
        'pokemons': pokemons
    }
    return render(request, 'listar_todos.html', contexto)


def listar_completo(request, id=None):
    if request.method == "GET" and id != None:
        pokemon = get_object_or_404(Pokemon, id=id)
        contexto = {
            'pokemon': pokemon
        }
        return render(request, 'pokemon_attr.html', contexto)
    else:
        pokemon_lista = Pokemon.objects.all().order_by('-nome')
        paginator = Paginator(pokemon_lista, 6)
        page = request.GET.get('page')
        pokemon = paginator.get_page(page)
        contexto = {
            'pokemons': pokemon
        }
        return render(request, 'listar_completo.html', contexto)
