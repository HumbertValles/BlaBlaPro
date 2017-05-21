# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import FavoriteTrip

from django.shortcuts import render

# Create your views here.
def FavoriteTripView(request):
    if request.method == 'POST':
        favorite_trip_form = FavoriteTrip()
        if favorite_trip_form.isvalid():
            user = request.user
            favorite_trip_form.user = user
            favorite_trip_form.save()