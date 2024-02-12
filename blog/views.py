from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


class BlogView(ListView):
    queryset = Blog.objects.order_by('-id')
    paginate_by = 12
    template_name = 'blog.html'



def detail_page(request, id):
    obj = get_object_or_404(Blog, pk=id)
    return render(request, 'blog-single.html', {'obj': obj})