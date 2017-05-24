# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FavoriteTrip(models.Model):
    departure_place = models.CharField(max_length=100)
    arrival_place = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    user = models.ForeignKey(User)


class Driver(models.Model):
    name = models.TextField(blank=False)
    age = models.IntegerField(blank=False)
    car = models.TextField(blank=True)
    score = models.FloatField(blank=True)


class TripsDone(models.Model):
    departure_place = models.TextField(max_length=100, blank=False)
    arrival_place = models.TextField(max_length=100, blank=False)
    price = models.FloatField(blank=False)
    departure_time = models.DateTimeField(blank=False)
    arrival_time = models.DateTimeField(blank=False)
    duration = models.TextField(blank=False)
    driver = models.ForeignKey(Driver, default=1)


class Reccomended(models.Model):
    driver = models.ForeignKey(Driver, blank=True)
    personalScore = models.FloatField()