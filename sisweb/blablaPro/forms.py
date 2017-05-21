from django import forms
from models import FavoriteTrip

class FavoriteTrip (forms.ModelForm):
    class Meta:
        model = FavoriteTrip
        fields = ('departure_place','arrival_place','departure_time')
