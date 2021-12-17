from django.contrib import admin
from .models import Pokemon, Healing, Armor

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Healing)
admin.site.register(Armor)