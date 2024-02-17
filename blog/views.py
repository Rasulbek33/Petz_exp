from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def search_blog(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        blogs = Blog.objects.filter(title__contains=searched)
        return render(request, 'search_blog.html', {'searched' : searched, 'blogs': blogs})
    else:
        return render(request, 'search_blog.html', {})


class BlogView(ListView):
    queryset = Blog.objects.order_by('-id')
    paginate_by = 12
    template_name = 'blog.html'



def detail_page(request, id):
    obj = get_object_or_404(Blog, pk=id)
    return render(request, 'blog-single.html', {'obj': obj})