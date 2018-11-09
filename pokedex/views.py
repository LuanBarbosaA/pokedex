from django.shortcuts import render
from .models import Pokemon
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
import pdb

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
        '''for movimento in pokemon.movimentos.all():
            print(movimento)
        pdb.set_trace()'''
        return render(request, 'pokemon_attr.html', contexto)
    else:
        pokemon_lista = Pokemon.objects.all().order_by('-nome')

        # quantidade de paginas
        paginator = Paginator(pokemon_lista, 6)
        # qual a pagina desejada que ele quer IR
        page = request.GET.get('page')
        # pagina atual
        pokemon = paginator.get_page(page)
        contexto = {
            'pokemons': pokemon
        }
        return render(request, 'listar_completo.html', contexto)
