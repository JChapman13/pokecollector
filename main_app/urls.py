from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemon/', views.pokedex, name='index'),
  path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
  path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
  path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
  path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
  path('pokemon/<int:pokemon_id>/add_healing/', views.add_healing, name='add_healing'),
  path('pokemon/<int:pokemon_id>/assoc_armor/<int:armor_id>/', views.assoc_armor, name='assoc_armor'),
  path('armor/', views.ArmorList.as_view(), name='armor_index'),
  path('armor/<int:pk>/', views.ArmorDetail.as_view(), name='armor_detail'),
  path('armor/create/', views.ArmorCreate.as_view(), name='armor_create'),
  path('armor/<int:pk>/update/', views.ArmorUpdate.as_view(), name='armor_update'),
  path('armor/<int:pk>/delete/', views.ArmorDelete.as_view(), name='armor_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
