from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:id>/', views.pokemon_by_id),
    path('pokemon/<str:name>', views.pokemon_by_name)
]