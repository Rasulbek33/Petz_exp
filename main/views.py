from django.shortcuts import render
from django.views.generic import ListView
from main.models import Home
from django.utils.translation import gettext as _





class Home(ListView):
    template_name = 'home.html'
    model = Home