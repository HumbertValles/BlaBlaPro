from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import *

urlpatterns = [
    url(r'^$',homepage),
    #url(r'^newfavtrip/', FavoriteTripView),
    url(r'^favtriplist/(?P<pk>\d+)/$',
        login_required(FavoriteTripListView.as_view()),
        name='trip_list'),
    url(r'^newfavtrip/(?P<pk>\d+)/$',
        login_required(CreateTrip.as_view()),
        name='trip_list'),
    ]