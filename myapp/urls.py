from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/',views.pokemon_all,name="pokemon"),
    path('pokemon/<int:id>/', views.pokemon_by_id),
    path('pokemon/<str:name>/', views.pokemon_by_name),
    path('pokedex/<int:id>/',views.pokedex_by_id),
    path('pokedex/<str:name>/',views.pokedex_by_name)
]