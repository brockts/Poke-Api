from django.shortcuts import render
from django.http import HttpResponse,Http404
import json,requests

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")


def pokemon_all(request):
    url:str = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1008"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        lista_pokemons:list = [pokemon["name"] for pokemon in data["results"]]
        return render(request,'pokemon_all.html',{
            "pokemons":lista_pokemons
        })
    else:
        raise Http404


def pokemon_by_id(request,id: int):
    url_pokeapi:str = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url_pokeapi)
    if response.status_code == 200:
        data = response.json()
        database:dict = {
            "id":data["id"],
            "name":data["name"],
            "weight":data["weight"],
            "height": data["height"],
            "abilities": [skill["ability"]["name"] for skill in data["abilities"]]
        }
        sprite:str = data['sprites']['front_default']
        return render(request, 'pokemon_id.html',{
            "database":database,
            "sprite":sprite
        })
    else:
        raise Http404
    

def pokemon_by_name(request,name:str):
    url_pokeapi:str = f"https://pokeapi.co/api/v2/pokemon/{name.casefold()}"
    response = requests.get(url_pokeapi)
    if response.status_code == 200:
        data = response.json()
        database:dict = {
            "id":data["id"],
            "name":data["name"],
            "weight":data["weight"],
            "height": data["height"],
            "abilities": [skill["ability"]["name"] for skill in data["abilities"]]
        }
        sprite:str = data['sprites']['front_default']
        return render(request, 'pokemon_name.html',{
            "database":database,
            "sprite":sprite
        })
    else:
        raise Http404
    
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