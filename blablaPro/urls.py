from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import *

urlpatterns = [

    url(r'^newfavtrip/', FavoriteTripView),
    url(r'^favtriplist/(?P<pk>\d+)/$',
        login_required(FavoriteTripListView.as_view()),
        name='homepage'),
    ]