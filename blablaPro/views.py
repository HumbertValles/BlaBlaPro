# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import FavoriteTrip
from forms import FavoriteTripForm

from django.shortcuts import render

# Create your views here.
def FavoriteTripView(request):
    if request.method == 'GET':
        return render(request, 'FavoriteTrip.html', {
            'TitleHeader': "Favorite trip",
            'PageTitle':"Add your favorite trip",
            'form': FavoriteTripForm()
        })
    elif request.method == 'POST':
        favorite_trip_form = FavoriteTripForm(request.POST)
        if favorite_trip_form.is_valid():
            user = request.user
            favorite_trip_form.user = user
            favorite_trip_form.save()
            #return redirect(profile) it will return to your profile with the new favorite trip added
        else:
            return render (request, 'FavoriteTrip.html',{
                'TitleHeader': "FavoriteTrip",
                'PageTitle': "Add your favorite trip",
                'form': favorite_trip_form
            })