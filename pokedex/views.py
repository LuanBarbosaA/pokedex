from django.shortcuts import render
from .models import Pokemon
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
from django.db.models import F
import pdb


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


def listar_completo(request, id=None, top=None, top2=None):
    if top == "top" and id==None and request.method == "GET":
        #pdb.set_trace()
        pokemon_top = Pokemon.objects.all().order_by("-ataque_fisica")
        contexto = {
            "pokemonTops": pokemon_top
        }
        return render(request, 'listar_completo.html', contexto)
    elif request.method == "GET" and id != None:
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
        paginator = Paginator(pokemon_lista, 6)
        page = request.GET.get('page')
        pokemon = paginator.get_page(page)
        contexto = {
            'pokemons': pokemon
        }
        return render(request, 'listar_completo.html', contexto)


def listar_top_attr(request, top2=None):
    if top2 == "True" and id == None and request.method == "GET":
        pdb.set_trace()
        pokemon_top_attr = Pokemon.objects.annotate(total=F("ataque_fisica") + F("defesa_fisica")).order_by("-total")
        contexto = {
            "pokemonTopAttrs": pokemon_top_attr
        }
        return render(request, 'listar_completo.html', contexto)