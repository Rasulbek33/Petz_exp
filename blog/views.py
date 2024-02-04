from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Blog

class BlogView(ListView):
    queryset = Blog.objects.order_by('-id')
    paginate_by = 6

    template_name = 'blog.html'
