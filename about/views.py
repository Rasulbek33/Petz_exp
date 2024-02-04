from django.shortcuts import render
from django.views.generic import ListView
from about.models import About

class AboutView(ListView):
    queryset = About.objects.order_by('-id')
    paginate_by = 6

    template_name = 'about.html'
