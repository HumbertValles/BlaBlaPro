# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import ListView
from models import FavoriteTrip
from forms import FavoriteTripForm

from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')
"""
@login_required
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
            favorite_trip = favorite_trip_form.save(commit=False)
            favorite_trip.user = request.user
            favorite_trip.save()
            return render(request,'FavoriteTripList')
        else:
            return render (request, 'FavoriteTrip.html',{
                'TitleHeader': "FavoriteTrip",
                'PageTitle': "Add your favorite trip",
                'form': favorite_trip_form
            })
"""

class CreateTrip(CreateView):
    model = FavoriteTrip
    template_name = 'FavoriteTrip.html'
    form_class = FavoriteTripForm
    success_url = "/favtriplist/1"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTrip, self).form_valid(form)

@login_required
def UserProfile(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        return render(request, 'profile.html',{
            'TitleHeader': "User profile",
            'PageTitle': "Profile",
            'username': username
        })

class FavoriteTripListView(ListView):
    model = FavoriteTrip
    template_name = 'FavoriteTripList.html'

    def get_context_data(self, **kwargs):
        context = super(FavoriteTripListView, self).get_context_data(**kwargs)
        favorite_trip = FavoriteTrip.objects.filter(user=self.request.user).order_by('departure_place')
        context['user_favorite_trip'] = list(favorite_trip)
        return context
