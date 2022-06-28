from django.shortcuts import get_object_or_404, render
from .models import Blog

def index(request):
    return render(request, "developer/index.html")

def about(request):
    return render(request, "developer/about.html")

def blog(request):
    blogs = Blog.objects
    return render(request, 'developer/blog.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'developer/detail.html', {'blog': blog_detail})

