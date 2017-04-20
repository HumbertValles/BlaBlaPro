# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blablaPro.models import FavoriteTrip,Driver,TripsDone,Reccomended
from django.contrib import admin

# Register your models here.

admin.site.register(FavoriteTrip)
admin.site.register(Driver)
admin.site.register(TripsDone)
admin.site.register(Reccomended)
