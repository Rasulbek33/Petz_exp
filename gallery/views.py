from django.shortcuts import render
from django.views.generic import ListView
from gallery.models import Gallery

class GalleryView(ListView):
    queryset = Gallery.objects.order_by('-id')
    paginate_by = 12

    template_name = 'gallery.html'
