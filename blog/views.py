from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog

class BlogView(ListView):
    queryset = Blog.objects.order_by('-id')
    paginate_by = 6

    template_name = 'blog.html'

class Lates_post(ListView):
    queryset = Blog.objects.order_by('-id')
    paginate_by = 6

    template_name = 'blog.html'

class About_us(ListView):
    paginate_by = 7
    template_name = 'blog.html'

class Author(ListView):
    paginate_by = 8
    template_name = 'blog.html'