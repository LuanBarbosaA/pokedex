"""PokemonCompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "pokedex"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('todos/', views.listar_todos, name="listar_todos"),
    path('listar/', views.listar_completo, name="listar"),
    path('listar/<str:top>', views.listar_completo, name="pokemonTop"),
    path('listar/<str:top2>', views.listar_top_attr, name="pokemonTopAttr"),
    path('pokemon/<int:id>', views.listar_completo, name="pokemon"),
]
