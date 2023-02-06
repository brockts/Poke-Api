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
    height_obtained = (float(data_list['height']) * 0.1)
    height_rounded = round(height_obtained, 2)
    weight_obtained = (float(data_list['weight']) * 0.1)
    weight_rounded = round(weight_obtained, 2)
    data = {
        "id": str(data_list['id']),
        "name": str(data_list['name']).capitalize(),
        "height": str(height_rounded)+ " m",
        "weight": str(weight_rounded)+ " kg",
        "sprite": str(data_list['sprites']['front_default']),
        }
    print(data)
    return render(request, 'pokemon_id.html',data)
def pokemon_by_name(request,name):
    url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{name.casefold()}/')
    url_pokeapi.add_header('User-Agent', "pikachu")
    source = urllib.request.urlopen(url_pokeapi).read()
    data_list = json.loads(source)
    height_obtained = (float(data_list['height']) * 0.1)
    height_rounded = round(height_obtained, 2)
    weight_obtained = (float(data_list['weight']) * 0.1)
    weight_rounded = round(weight_obtained, 2)
    data = {
        "id": str(data_list['id']),
        "name": str(data_list['name']).capitalize(),
        "height": str(height_rounded)+ " m",
        "weight": str(weight_rounded)+ " kg",
        "sprite": str(data_list['sprites']['front_default']),
        }
    print(data)
    return render(request, 'pokemon_name.html',data)