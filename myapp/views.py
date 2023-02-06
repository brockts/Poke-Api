from django.shortcuts import render
from django.http import HttpResponse
import urllib.request,json

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")
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