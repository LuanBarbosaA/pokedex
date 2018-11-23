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


def listar_completo(request, id=None, top=None):
    if top == 1 and id==None and request.method == "GET":
        pokemon = Pokemon.objects.all().order_by("-ataque_fisica")
        paginator = Paginator(pokemon, 6)
        page = request.GET.get('page')
        pokemon_top = paginator.get_page(page)
        contexto = {
            "pokemonTops": pokemon_top
        }
        return render(request, 'listar_completo.html', contexto)
    elif top == 2 and id == None and request.method == "GET":
        pokemon = Pokemon.objects.annotate(total=F("ataque_fisica") + F("defesa_fisica") + F("ataque_especial") + F("defesa_especial") + F("vida") + F("velocidade") + F("experiencia") + F("peso") + F("habilidades")).order_by("-total")
        paginator = Paginator(pokemon, 6)
        page = request.GET.get('page')
        pokemon_top_attr = paginator.get_page(page)
        contexto = {
            "pokemonTopAttrs": pokemon_top_attr
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
        pokemon_lista = Pokemon.objects.all().order_by('-nome').reverse()
        paginator = Paginator(pokemon_lista, 6)
        page = request.GET.get('page')
        pokemon = paginator.get_page(page)
        contexto = {
            'pokemons': pokemon
        }
        return render(request, 'listar_completo.html', contexto)