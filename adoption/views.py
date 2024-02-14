from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from adoption.models import Adoption, Adoption_name


class AdoptionView(ListView):
    template_name = 'adoption.html'

    def get_queryset(self):
        qs = Adoption.objects.all()
        return qs

class Adoption_nameView(ListView):
    template_name = 'adoption.html'


    def get_queryset(self):
        qs = Adoption_name.objects.all()
        return qs
