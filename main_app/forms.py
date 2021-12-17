from django.forms import ModelForm
from .models import Healing

class HealingForm(ModelForm):
  class Meta:
        model = Healing
        fields = ['date', 'heal_stats']