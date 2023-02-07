from django.shortcuts import render
from django.http import HttpResponse,Http404
import requests

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
            "weight":str(round((data["weight"])*0.1,2))+ " kg",
            "height": str(round((data["height"])*0.1,2))+ " m",
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
            "weight":str(round((data["weight"])*0.1,2))+ " kg",
            "height": str(round((data["height"])*0.1,2))+ " m",
            "abilities": [skill["ability"]["name"] for skill in data["abilities"]]
        }
        sprite:str = data['sprites']['front_default']
        return render(request, 'pokemon_name.html',{
            "database":database,
            "sprite":sprite
        })
    else:
        raise Http404
    
def pokedex_all(request):
    url_pokeapi:str = "https://pokeapi.co/api/v2/pokedex/?offset=0&limit=30"
    response = requests.get(url_pokeapi)
    if response.status_code==200:
        data = response.json()
        lista_regions:list = [region["name"] for region in data["results"]]
        return render(request,"pokedex_all.html",{
            "regions":lista_regions
        })
    else:
        raise Http404
    

def pokedex_by_id(request, id:int):
    url_pokeapi:str = f"https://pokeapi.co/api/v2/pokedex/{id}"
    response = requests.get(url_pokeapi)
    if response.status_code==200:
        data = response.json()
        database:dict = {
            "name":data["descriptions"][2]["description"],
            "pokemon_by_region": [pokemon["pokemon_species"]["name"] for pokemon in data["pokemon_entries"]]
        }
        return render(request,"pokedex_id.html",{
            "database":database
        })
    else:
        raise Http404

def pokedex_by_name(request,name:str):
    url_pokeapi:str = f"https://pokeapi.co/api/v2/pokedex/{name.casefold()}"
    response = requests.get(url_pokeapi)
    if response.status_code==200:
        data = response.json()
        database:dict = {
            "name":data["descriptions"][2]["description"],
            "pokemon_by_region": [pokemon["pokemon_species"]["name"] for pokemon in data["pokemon_entries"]]
        }
        return render(request,"pokedex_id.html",{
            "database":database
        })
    else:
        raise Http404