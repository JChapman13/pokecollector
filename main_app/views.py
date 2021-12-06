from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

def pokedex(request):
  return render(request, 'pokemon/pokedex.html', { 'pokemon': pokemon })

class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, poketype, species, ability):
    self.name = name
    self.poketype = poketype
    self.species = species
    self.ability = ability

pokemon = [
  Pokemon('Bulbasaur', 'Grass/Poison', 'Seed', "Overgrow"),
  Pokemon('Charmander', 'Fire', 'Lizard', "Blaze"),
  Pokemon('Squirtle', 'Water', 'Tiny Turtle', "Torrent")
]