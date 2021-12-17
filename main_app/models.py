from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

HEAL_STATS = (
    ("H", "Health"),
    ("M", "Mana"),
    ("F", "Full Restore")
)

# Create your models here.
class Armor(models.Model):
    name = models.CharField(max_length=250)
    main_stats = models.CharField(max_length=250) 
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('armor_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    poketype = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    armor = models.ManyToManyField(Armor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

    def healed_for_today(self):
        return self.healing_set.filter(date=date.today()).count() >=len(HEAL_STATS)

class Healing(models.Model):
    date = models.DateField('healing date')
    heal_stats = models.CharField(max_length=1, choices=HEAL_STATS, default=HEAL_STATS[0][0])
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_heal_stats_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
