from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Armor
from .forms import HealingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PokemonCreate(LoginRequiredMixin, CreateView):
  model = Pokemon
  fields = '__all__'

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PokemonUpdate(LoginRequiredMixin, UpdateView):
  model = Pokemon
  fields = ['poketype', 'species', 'ability']

class PokemonDelete(LoginRequiredMixin, DeleteView):
  model = Pokemon
  success_url = "/pokemon/"

@login_required
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def pokedex(request):
  pokemon = Pokemon.objects.filter(user=request.user)
  return render(request, 'pokemon/pokedex.html', { 'pokemon': pokemon })

@login_required
def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  armor_pokemon_doesnt_have = Armor.objects.exclude(id__in = pokemon.armor.all().values_list('id'))
  healing_form = HealingForm()
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon, 'healing_form': healing_form, 'armor': armor_pokemon_doesnt_have})

@login_required
def add_healing(request, pokemon_id):
  form = HealingForm(request.POST)
  if form.is_valid():
    new_healing = form.save(commit=False)
    new_healing.pokemon_id = pokemon_id
    new_healing.save()
  return redirect('detail', pokemon_id=pokemon_id)

@login_required
def assoc_armor(request, pokemon_id, armor_id):
  Pokemon.objects.get(id=pokemon_id).armor.add(armor_id)
  return redirect('detail', pokemon_id=pokemon_id)

class ArmorList(LoginRequiredMixin, ListView):
  model = Armor

class ArmorDetail(LoginRequiredMixin, DetailView):
  model = Armor

class ArmorCreate(LoginRequiredMixin, CreateView):
  model = Armor
  fields = '__all__'

class ArmorUpdate(LoginRequiredMixin, UpdateView):
  model = Armor
  fields = ['name', 'main_stats']

class ArmorDelete(LoginRequiredMixin, DeleteView):
  model = Armor
  success_url = '/armor/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error-message': error_message}
  return render(request, 'registration/signup.html', context)