from django.shortcuts import render
from django.http import HttpResponse
import urllib.request,json,requests

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")
def pokemon_all(request):
    url = "https://pokeapi.co/api/v2/pokemon/"
    solicitud = requests.get(url)
    data = solicitud.json()
    lista_pokemons = [pokemon["name"] for pokemon in data["results"]]
    return render(request,'pokemon_all.html',{
        "pokemons":lista_pokemons
    })


def pokemon_by_id(request,id):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{id}/')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    data_list = json.loads(source)
    data = {
        "id": str(data_list['id']),
        "name": str(data_list['name']).capitalize(),
        "height": str(round(float(data_list["height"])*0.1,2))+ " m",
        "weight": str(round(float(data_list["weight"])*0.1,2))+ " kg",
        "sprite": str(data_list['sprites']['front_default']),
        }
    return render(request, 'pokemon_id.html',data)

def pokemon_by_name(request,name):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{name.casefold()}/')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    data_list = json.loads(source)
    data = {
        "id": str(data_list['id']),
        "name": str(data_list['name']).capitalize(),
        "height": str(round(float(data_list["height"])*0.1,2))+ " m",
        "weight": str(round(float(data_list["weight"])*0.1,2))+ " kg",
        "sprite": str(data_list['sprites']['front_default']),
        }
    return render(request, 'pokemon_name.html',data)
def pokedex_by_id(request,id):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokedex/{id}/')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    data_list = json.loads(source)
    database = {
        "description": str(data_list['descriptions'][2]["description"]),
        "pokemon_entries": str(data_list['pokemon_entries'])
    }
    return render(request,"pokedex_id.html",{
        "database":database
    })
def pokedex_by_name(request,name):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokedex/{id}/')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    data_list = json.loads(source)
    database = {
        "description": str(data_list['descriptions'][2]["description"]),
        "pokemon_entries": str(data_list['pokemon_entries'])
    }
    return render(request,"pokedex_id.html",{
        "database":database
    })